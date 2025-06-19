# 📚 Book Scraper & Search Web App | Cantilever Internship Task 1

This project is a complete data pipeline that scrapes book data from [BooksToScrape.com](https://books.toscrape.com), stores it in CSV, and displays it in a simple, searchable web interface using Flask.

---

## 🛠️ What I Did

As part of **Task 1: Web Scraping**, I completed the following:

- ✅ Scraped product data from a real website using `requests` + `BeautifulSoup`
- ✅ Extracted Title, Price, Rating, Availability, Category, Description, and Product Link
- ✅ Stored the data in a CSV file (`books.csv`)
- ✅ Built a simple Flask-based web interface (`app.py`) to:
  - View all books
  - Search books by Title or Category
- ✅ Implemented frontend using `Jinja2` + `HTML` template
- ✅ Generated `requirements.txt` for dependency management

---

## 📦 Technologies Used

| Tool/Lib        | Purpose                        |
|-----------------|--------------------------------|
| `Python 3.11`   | Main language                  |
| `requests`      | To fetch HTML content          |
| `BeautifulSoup` | To parse and extract data      |
| `pandas`        | To store, filter, and clean data |
| `Flask`         | To build the web interface     |
| `HTML/CSS`      | UI styling and templating      |

---

## 🚀 How to Run This Project

> 💡 Make sure Python 3.10+ is installed.

### 1. Clone the repo
- git clone https://github.com/your-username/CANTILEVER.git
- cd CANTILEVER/Task_1_WebScrapping

### 2. Install requirements
pip install -r requirements.txt

### 3. Start the Flask server
python app.py
