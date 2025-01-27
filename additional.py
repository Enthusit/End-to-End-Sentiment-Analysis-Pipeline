import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
db_name = "imdb_reviews.db"  # Ensure this is your correct database file name
connection = sqlite3.connect(db_name)

# Load data from the reviews table
df = pd.read_sql_query("SELECT sentiment, cleaned_text FROM reviews", connection)

# Calculate the distribution of reviews per sentiment
sentiment_counts = df["sentiment"].value_counts()

# Close the database connection
connection.close()

# Plot sentiment distribution
sentiment_counts.plot(kind="bar", color=["skyblue", "salmon"])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.show()


from wordcloud import WordCloud

# Generate a word cloud for positive reviews
positive_reviews = " ".join(df[df["sentiment"] == "positive"]["cleaned_text"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(positive_reviews)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud for Positive Reviews")
plt.show()
