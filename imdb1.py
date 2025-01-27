import sqlite3
import pandas as pd

# Step 1: Connect to SQLite database (or create a new one)
conn = sqlite3.connect("imdb_reviews.db")
cursor = conn.cursor()

# Step 2: Create the 'reviews' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    review TEXT NOT NULL,
    sentiment TEXT NOT NULL
)
''')

# Step 3: Load dataset (assumes CSV file with columns: review_id, review, sentiment)
df = pd.read_csv("/Users/basiljoy/Downloads/IMDB Dataset.csv")

# Step 4: Insert data into the 'reviews' table
df.to_sql("reviews", conn, if_exists="append", index=False)

# Step 5: Confirm data insertion
cursor.execute("SELECT COUNT(*) FROM reviews")
print(f"Number of records in 'reviews' table: {cursor.fetchone()[0]}")

# Step 6: Close the connection
conn.commit()
conn.close()
