import sqlite3
import re
import string

# Function to clean text
def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# Connect to the database
db_name = "imdb_reviews.db"  # Database name
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Add a new column for cleaned text if it doesn't already exist
try:
    cursor.execute("ALTER TABLE reviews ADD COLUMN cleaned_text TEXT")
    connection.commit()
except sqlite3.OperationalError:
    print("Column 'cleaned_text' already exists. Skipping this step.")

# Fetch all reviews and clean them
cursor.execute("SELECT review_id, review FROM reviews")
rows = cursor.fetchall()

for row in rows:
    review_id, review_text = row
    cleaned = clean_text(review_text)
    cursor.execute(
        "UPDATE reviews SET cleaned_text = ? WHERE review_id = ?", (cleaned, review_id)
    )

# Commit changes and close the connection
connection.commit()
connection.close()

print("Data cleaning completed and stored in 'cleaned_text' column.")
