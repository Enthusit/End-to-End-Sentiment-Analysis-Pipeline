import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Data from SQLite Database
db_name = "imdb_reviews.db"  # Ensure this matches your database file
connection = sqlite3.connect(db_name)

# Load the cleaned text and sentiment columns
df = pd.read_sql_query("SELECT cleaned_text, sentiment FROM reviews", connection)
connection.close()

# Step 2: Encode Sentiments
# Convert sentiments to binary values (positive = 1, negative = 0)
df["sentiment"] = df["sentiment"].apply(lambda x: 1 if x == "positive" else 0)

# Step 3: Split Data into Train/Test Sets
X = df["cleaned_text"]  # Feature: cleaned review text
y = df["sentiment"]     # Label: sentiment (1 = positive, 0 = negative)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Vectorize Text Data using TF-IDF
tfidf = TfidfVectorizer(max_features=5000)  # Limit to top 5000 features
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Step 5: Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test_tfidf)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Optional: Save the model and TF-IDF vectorizer for later use
import joblib
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(tfidf, "tfidf_vectorizer.pkl")
