# OCR Web App (Flask + Tesseract)

A simple web application to extract text from images, PDF, and DOCX files using **Tesseract OCR** and **Flask**.  
It also supports exporting the extracted text to **PDF** and **DOCX**.

---

## 🚀 Features
- Upload **Image (JPG, PNG)**, **PDF**, or **DOCX** file
- Extract text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Supports **English language**
- Download extracted text as:
  - Plain text (shown on webpage)
  - PDF file
  - Word file (DOCX)
- Clean and simple UI (Flask + HTML + Bootstrap)

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **OCR Engine**: Tesseract OCR (`pytesseract`)
- **File Handling**: python-docx, reportlab, pdf2image
- **Frontend**: HTML + Bootstrap
- **Extras**: OpenCV (image preprocessing)

---

## 📂 Project Structure
