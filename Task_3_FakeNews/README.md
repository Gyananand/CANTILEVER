# 📰 Fake News Detector

A simple Machine Learning web app that detects whether a news article is **Fake** or **Real** using Python, Scikit-learn, and Flask.

---

## 📂 Project Structure
```

Task\_3\_FakeNews/
│── app.py              # Flask web app
│── train\_model.py      # Script to train model and save model.pkl, tfidf.pkl
│── model.pkl           # Trained ML model
│── tfidf.pkl           # Saved TF-IDF vectorizer
│── templates/
│   └── index.html      # Frontend (HTML page)
│── static/             # (Optional: add CSS/JS here)
│── True.csv            # Real news dataset
│── Fake.csv            # Fake news dataset
│── README.md           # Project documentation

````

---

## ⚙️ Installation & Setup

### 1. Clone repo or copy files
```bash
git clone <your-repo-link>
cd Task_3_FakeNews
````

### 2. Create Virtual Environment (Python 3.12.4)

```bash
python -m venv .venv
```

Activate it:

* Windows (PowerShell):

  ```bash
  .venv\Scripts\activate
  ```
* Linux/Mac:

  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install flask scikit-learn pandas numpy
```

---

## 🏋️ Train the Model

Run the training script:

```bash
python train_model.py
```

This will generate:

* `model.pkl`
* `tfidf.pkl`

---

## 🚀 Run the Web App

Start Flask:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🖊️ Usage

* Paste any news text/article into the input box.
* Click **Predict**.
* The app will show:

  * ✅ **Real News**
  * ❌ **Fake News**

---

## 📊 Dataset

We used Kaggle’s **Fake and Real News Dataset**:

* `True.csv` → real news
* `Fake.csv` → fake news

Each file has columns: `title`, `text`, `subject`, `date`.

---

## ✅ Example

Input:

```
India successfully landed its Chandrayaan-3 mission on the Moon.
```

Output:

```
✅ Real News
```

Input:

```
Aliens landed in Delhi yesterday.
```

Output:

```
❌ Fake News
```

---

## 🛠️ Tech Stack

* Python 3.12.4
* Flask
* Scikit-learn (LinearSVC, TfidfVectorizer)
* Pandas, NumPy

---

## 📌 Next Steps

* Improve UI (add CSS/Bootstrap)
* Deploy to **Heroku / Render / PythonAnywhere**
* Add real-time news scraping

---

👨‍💻 Developed by \[Gyan Anand]

```

---

👉 Do you want me to also create a `requirements.txt` for you so you can install everything in one command?
```
