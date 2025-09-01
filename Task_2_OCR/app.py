from flask import Flask, render_template, request, send_from_directory, flash, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import Image
import cv2
import numpy as np
from io import BytesIO
from reportlab.pdfgen import canvas

# ====== CONFIG ======
web = Flask(__name__)
web.secret_key = "cantilever-task2-ocr"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

web.config["UPLOAD_FOLDER"] = UPLOAD_DIR
web.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTS = {"png", "jpg", "jpeg", "bmp", "tiff", "webp"}

# Point to Tesseract binary on Windows if needed:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTS


def preprocess_for_ocr(pil_img: Image.Image) -> Image.Image:
    """Basic preprocessing to improve OCR results."""
    img = np.array(pil_img)
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    thr = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11
    )
    den = cv2.fastNlMeansDenoising(thr, h=20)

    return Image.fromarray(den)


def draw_bounding_boxes(pil_img: Image.Image):
    """Return OpenCV image with bounding boxes drawn (English only)."""
    img = np.array(pil_img.convert("RGB"))
    data = pytesseract.image_to_data(pil_img, lang="eng", output_type=pytesseract.Output.DICT)

    for i in range(len(data["text"])):
        try:
            conf = int(data["conf"][i])
            if conf > 50:  # only confident detections
                x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        except (ValueError, TypeError):
            continue

    return Image.fromarray(img)


@web.route("/", methods=["GET", "POST"])
def index():
    extracted_text = None
    uploaded_filename = None
    ocr_confidence = None
    error_msg = None

    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part in request.")
            return redirect(request.url)
        f = request.files["file"]
        if f.filename == "":
            flash("No file selected.")
            return redirect(request.url)
        if not allowed_file(f.filename):
            flash("Unsupported file type.")
            return redirect(request.url)

        filename = secure_filename(f.filename)
        save_path = os.path.join(UPLOAD_DIR, filename)
        f.save(save_path)
        uploaded_filename = filename

        try:
            pil_img = Image.open(save_path)
            pil_proc = preprocess_for_ocr(pil_img)

            # English only
            extracted_text = pytesseract.image_to_string(pil_proc, lang="eng")

            # OCR confidence
            data = pytesseract.image_to_data(
                pil_proc, lang="eng", output_type=pytesseract.Output.DICT
            )

            confs = []
            for c in data.get("conf", []):
                try:
                    c_int = int(c)
                    if c_int >= 0:
                        confs.append(c_int)
                except (ValueError, TypeError):
                    continue

            if confs:
                ocr_confidence = round(sum(confs) / len(confs), 1)

            # Save bounding box preview
            boxed_img = draw_bounding_boxes(pil_proc)
            boxed_path = os.path.join(UPLOAD_DIR, "boxed_" + filename)
            boxed_img.save(boxed_path)

            # Save OCR result to a .txt file
            txt_path = os.path.join(UPLOAD_DIR, "ocr_" + os.path.splitext(filename)[0] + ".txt")
            with open(txt_path, "w", encoding="utf-8") as tf:
                tf.write(extracted_text)

        except Exception as e:
            error_msg = f"OCR failed: {e}"

    return render_template(
        "index.html",
        text=extracted_text,
        filename=uploaded_filename,
        confidence=ocr_confidence,
        error=error_msg
    )


# ===== EXPORT ROUTES =====

@web.route("/download/txt/<filename>")
def download_txt(filename):
    path = os.path.join(UPLOAD_DIR, filename)
    return send_file(path, as_attachment=True, download_name="ocr_result.txt")


@web.route("/download/pdf", methods=["POST"])
def download_pdf():
    text = request.form.get("ocr_text", "")
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(72, 800, "OCR Extracted Text")
    y = 780
    for line in text.splitlines():
        c.drawString(72, y, line)
        y -= 14
    c.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="ocr_result.pdf", mimetype="application/pdf")


@web.route("/download/docx", methods=["POST"])
def download_docx():
    text = request.form.get("ocr_text", "")
    doc = Document()
    doc.add_heading("OCR Extracted Text", level=1)
    doc.add_paragraph(text)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="ocr_result.docx", mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


@web.route("/uploads/<path:name>")
def uploaded_file(name):
    return send_from_directory(UPLOAD_DIR, name)


if __name__ == "__main__":
    web.run(debug=True)
