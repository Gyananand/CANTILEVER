# 📝 OCR Web App 

A simple web application to extract text from images, PDFs, and DOCX files using **Tesseract OCR** and **Flask**.  
It also supports exporting the extracted text to **PDF** and **DOCX** formats.

---

## 🚀 Features
- Upload **Image (JPG, PNG)**, **PDF**, or **DOCX** files  
- Extract text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
- Supports **English language**  
- Download extracted text as:  
  - Plain text (shown on webpage)  
  - PDF file  
  - Word file (DOCX)  
- Clean and simple UI (Flask + HTML + Bootstrap)

---

## 🛠 Tech Stack
- **Backend**: Flask (Python)  
- **OCR Engine**: Tesseract OCR (`pytesseract`)  
- **File Handling**: `python-docx`, `reportlab`, `pdf2image`  
- **Frontend**: HTML + Bootstrap  
- **Extras**: OpenCV (for image preprocessing)

---

## 📂 Project Structure
```

Task\_2\_OCR/
│── app.py                # Flask app entry point
│── requirements.txt      # Dependencies
│── templates/
│   └── index.html        # Web UI template
│── uploads/              # Uploaded files
│── README.md             # Documentation

````

---

## ⚙️ Installation & Usage

1. Clone this repository and navigate to the OCR task folder:
   ```bash
   git clone https://github.com/your-username/CANTILEVER.git
   cd CANTILEVER/Task_2_OCR
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure **Tesseract OCR** is installed:

   * [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
   * Add it to your system PATH

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📸 Example Workflow

1. Upload an image, PDF, or DOCX file
2. The app extracts text using OCR
3. View text directly on the webpage
4. Download text as PDF or DOCX

---

## 🎯 Future Improvements

* Add support for multiple languages
* Improve OCR accuracy with advanced preprocessing
* Deploy on Heroku or any cloud platform

---

## 👨‍💻 Author

Developed as part of **Cantilever Internship** Task 2.

```