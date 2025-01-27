# End-to-End-Sentiment-Analysis-Pipeline

Overview
This project implements an end-to-end sentiment analysis pipeline using the IMDB movie reviews dataset. It includes:

1.Data ingestion and database setup (SQLite).
2.Data cleaning and exploration.
3.Sentiment classification using Logistic Regression with TF-IDF features.
4.A Flask API to serve the trained model for sentiment prediction.

app.py                  # Flask application for the API
imdb1.py                # Script to set up the database and ingest data
model.py                # Script to train and save the classification model
additional.py           # Script for plotting the number of positive and negative reviews
imdb_reviews.db         # SQLite database file (created by i,db1.py)
requirements.txt        # Python dependencies
cleaned.py              # Database cleaned by removing the html tags etc.
EDA.py                  # It is used to find the average count of the sentiments
req.py                  # It is used to send a POST request to analyse the review

README.md 

Getting Started
1.
Prerequisites
Python 3.8+
SQLite installed (pre-installed on most systems)

pip install -r requirements.txt

2Dataset
The IMDB dataset is used for this project. The dataset is downloaded from Kaggle in imdb1.py.
Steps to Run the Project
i. Data Setup
Run imdb1.py to:

Download the IMDB dataset (25k reviews with sentiment labels) from Kaggle.

Run cleaned.py to:

Clean and preprocess the data.
Insert the cleaned data into the SQLite database (imdb_reviews.db).


ii. Exploratory Data Analysis
Run additional.py to:

Perform basic exploratory data analysis (EDA) such as:
Sentiment distribution.
Average review length by sentiment.
Generate visualizations.

python EDA.py
python additional.py

iii. Train the Model
Run model.py to:

Load data from the SQLite database.
Train a Logistic Regression model using TF-IDF features.
Save the trained model to model.pkl.

python train_model.py

iv. Start the Flask API
Run app.py to start the Flask API for serving predictions.

python app.py


v. Test the API
Use the /predict endpoint to test the API. You can send a POST request with a review text and receive the predicted sentiment.

Run req.py to:

Send a POST request to analyse the sentiment.


3.
Database Details
Database Name
              imdb_reviews.db
Schema
The reviews table schema is as follows:

CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    review_text TEXT NOT NULL,
    sentiment TEXT NOT NULL
);


4.
Model Details
Type: Logistic Regression
Features: TF-IDF (Term Frequency-Inverse Document Frequency)
Training Accuracy: ~92%
Test Accuracy: ~88%
Evaluation Metrics:
F1 Score, Precision, Recall available in model.py.

5.
Requirements
The dependencies are listed in requirements.txt. Install them with:

pip install -r requirements.txt




