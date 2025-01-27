from flask import Flask, request, jsonify
import joblib
import re
import string

# Load the trained model and TF-IDF vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)

# Function to clean text (same as in training step)
def clean_text(text):
    text = text.lower()  # Lowercase
    text = re.sub(r"<[^>]+>", "", text)  # Remove HTML tags
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    return text


@app.route('/')
def home():
    return 'You are in Home-Page'
# Define the /predict endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the input text from the POST request
        data = request.get_json()
        review_text = data["review_text"]

        # Clean the input text
        cleaned_review = clean_text(review_text)

        # Vectorize the cleaned text using the loaded TF-IDF vectorizer
        review_tfidf = tfidf.transform([cleaned_review])

        # Predict sentiment (1 = positive, 0 = negative)
        prediction = model.predict(review_tfidf)

        # Return the prediction as JSON
        sentiment = "positive" if prediction[0] == 1 else "negative"
        return jsonify({"sentiment_prediction": sentiment})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)