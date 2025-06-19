import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

HOME_URL = "https://books.toscrape.com/"
MAIN_PAGE = "https://books.toscrape.com/index.html"
PAGINATED_LINK = "https://books.toscrape.com/catalogue/page-{}.html"

custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def extract_star_rating(rating_tag):
    if rating_tag:
        tag_classes = rating_tag.get("class", [])
        for level in ['One', 'Two', 'Three', 'Four', 'Five']:
            if level in tag_classes:
                return level
    return "N/A"

def fetch_description_and_genre(detail_page_url):
    try:
        page_resp = requests.get(detail_page_url, headers=custom_headers)
        detail_soup = BeautifulSoup(page_resp.text, 'lxml')

        meta_tag = detail_soup.find("meta", attrs={"name": "description"})
        book_summary = meta_tag['content'].strip() if meta_tag else "No description"

        genre_path = detail_soup.select("ul.breadcrumb li")[2].text.strip()

        return book_summary, genre_path
    except:
        return "Error fetching description", "Unknown"

book_inventory = []
current_page = 1
collected_books = 0
BOOK_LIMIT = 100

print("Launching scrape on BooksToScrape (Limit: 100 books)...")

while collected_books < BOOK_LIMIT:
    target_url = MAIN_PAGE if current_page == 1 else PAGINATED_LINK.format(current_page)
    print(f"Accessing page {current_page} : {target_url}")

    page_resp = requests.get(target_url, headers=custom_headers)
    if page_resp.status_code != 200:
        print("Page not reachable.")
        break

    page_soup = BeautifulSoup(page_resp.text, 'lxml')
    book_blocks = page_soup.find_all("article", class_="product_pod")

    if not book_blocks:
        break  # No further content

    for entry in book_blocks:
        if collected_books >= BOOK_LIMIT:
            break

        try:
            book_title = entry.h3.a["title"]
            book_price = entry.find("p", class_="price_color").text.strip()
            stock_status = entry.find("p", class_="instock availability").text.strip()
            book_rating = extract_star_rating(entry.find("p", class_="star-rating"))

            # Product link setup
            raw_link = entry.h3.a["href"]
            final_link = raw_link.replace("../../", "catalogue/")
            full_product_url = HOME_URL + final_link

            # Scrape book detail page
            book_desc, book_genre = fetch_description_and_genre(full_product_url)

            book_inventory.append({
                "Title": book_title,
                "Price": book_price,
                "Rating": book_rating,
                "Availability": stock_status,
                "Product Link": full_product_url,
                "Description": book_desc,
                "Category": book_genre
            })

            collected_books += 1
            print(f"[{collected_books}] {book_title}")

        except Exception as err:
            print(f"Failed on book #{collected_books + 1}: {err}")
            continue

    current_page += 1
    time.sleep(1)  # Rate limiting

# Export scraped data
book_data = pd.DataFrame(book_inventory)
book_data.to_csv("books.csv", index=False)
print(f"\n Extraction complete — {collected_books} books saved to books.csv")
