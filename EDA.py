import pandas as pd
import sqlite3

# Connect to the database
db_name = "imdb_reviews.db"  # Database name
connection = sqlite3.connect(db_name)

# Load the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT sentiment, cleaned_text FROM reviews", connection)

# Distribution of reviews per sentiment
sentiment_counts = df["sentiment"].value_counts()
print("Sentiment Distribution:")
print(sentiment_counts)

# Average review length by sentiment
df["review_length"] = df["cleaned_text"].apply(len)
average_lengths = df.groupby("sentiment")["review_length"].mean()
print("\nAverage Review Length by Sentiment:")
print(average_lengths)

# Close the connection
connection.close()
