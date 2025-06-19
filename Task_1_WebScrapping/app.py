from flask import Flask, render_template, request
import pandas as pd

# Initialize Flask app
web_app = Flask(__name__)

# Load book dataset
catalog_data = pd.read_csv("books.csv")

@web_app.route('/', methods=['GET'])
def homepage():
    search_term = request.args.get('query', '').lower()

    if search_term:
        matching_books = catalog_data[
            catalog_data['Title'].str.lower().str.contains(search_term) |
            catalog_data['Category'].str.lower().str.contains(search_term)
        ]
    else:
        matching_books = catalog_data

    return render_template(
        'index.html',
        books=matching_books.to_dict(orient='records'),
        query=search_term
    )

if __name__ == '__main__':
    web_app.run(debug=True)
