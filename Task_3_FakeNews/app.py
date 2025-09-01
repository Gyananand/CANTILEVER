from flask import Flask, render_template, request
import pickle

# Load model and TF-IDF
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    user_input = ""
    
    if request.method == "POST":
        user_input = request.form["news"]
        vector = tfidf.transform([user_input])
        result = model.predict(vector)[0]
        
        # Map 0 → FAKE, 1 → REAL
        prediction = "REAL" if result == 1 else "FAKE"
    
    return render_template("index.html", prediction=prediction, news=user_input)

if __name__ == "__main__":
    app.run(debug=True)
