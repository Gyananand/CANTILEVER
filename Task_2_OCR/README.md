# 📝 OCR Web App

A lightweight and intuitive **Flask web application** that extracts text from **images, PDFs, and DOCX files** using **Tesseract OCR**.
It also allows exporting the extracted text into **PDF** and **Word (DOCX)** formats.

---

## 🚀 Features

* 📤 Upload **Images (JPG, PNG)**, **PDF**, or **DOCX** files
* 🔍 Extract text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* 🌐 Supports **English language OCR**
* 💾 Export extracted text as:

  * Plain text (shown on webpage)
  * **PDF** file
  * **Word (DOCX)** file
* 🎨 Simple & clean web interface (Flask + Bootstrap)

---

## 🛠 Tech Stack

* **Backend**: Flask (Python)
* **OCR Engine**: Tesseract OCR (`pytesseract`)
* **File Handling**: `python-docx`, `reportlab`, `pdf2image`
* **Image Preprocessing**: OpenCV
* **Frontend**: HTML + Bootstrap

---

## 📂 Project Structure

```bash
Task_2_OCR/
│── app.py                # Flask application
│── requirements.txt      # Python dependencies
│── templates/
│   └── index.html        # Web UI template
│── uploads/              # Uploaded files (temporary storage)
│── README.md             # Project documentation
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/CANTILEVER.git
cd CANTILEVER/Task_2_OCR
```

### 2️⃣ Create & activate virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate  

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Tesseract OCR

* [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* Add Tesseract to your **system PATH**

### 5️⃣ Run the Flask app

```bash
python app.py
```

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📸 Example Workflow

1. Upload an **image**, **PDF**, or **DOCX** file
2. The app extracts text using OCR
3. Text appears on the webpage instantly
4. Option to **download text as PDF or DOCX**

---

## 🎯 Future Enhancements

* 🌍 Multi-language OCR support
* 🤖 Advanced preprocessing for better accuracy
* ☁️ Deploy on **Heroku / Render / AWS**
* 📱 Mobile-friendly responsive UI

---

## 👨‍💻 Author

Developed as part of **Cantilever Internship – Task 2** ✨
👉 Would you like me to also design a **badge section** (Python version, Flask, Tesseract, etc.) at the top like many popular GitHub repos? That makes the README look even more professional.
