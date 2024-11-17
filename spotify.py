import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Prompt the user for the CSV file name
csv_file = input("Please enter the file name (with .csv extension) of your liked songs playlist: ")


# Load CSV into pandas
df = pd.read_csv(csv_file)

# Creating a new SQL database called songs.db
conn = sqlite3.connect("songs.db")
cursor = conn.cursor()  # object kind of like a pointer that helps in executing queries and fetching results

# Drop the table if it already exists to avoid schema issues
cursor.execute('DROP TABLE IF EXISTS playlists')

# Recreate the table with the new column 'popularity'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS playlists (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         song_name TEXT,
         danceability REAL,
         energy REAL,
         loudness REAL,
         popularity REAL,
         liked INTEGER         
    )
''')

# Inserting CSV data into SQLite database
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO playlists (song_name, danceability, energy, loudness, popularity, liked)
        VALUES (?,?,?,?,?,?)
    ''' , (row['song_name'], row['danceability'], row['energy'], row['loudness'], row['popularity'], row['liked']))

# Commit changes to the database
conn.commit()

# MACHINE LEARNING SECTION
X = df[['danceability', 'energy', 'loudness', 'popularity']]  # selects columns as features
y = df["liked"]  # selects the 'liked' column as target

# Splitting data into training and test sets (80% training and 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()  # Creates an instance of logistic regression model
model.fit(X_train, y_train)  # Training the model

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Function to fetch data from the database (now including 'popularity')
def fetch_ml_data():
    cursor.execute('SELECT song_name, danceability, energy, loudness, popularity, liked FROM playlists')
    data = cursor.fetchall()  # Retrieve all rows from the query result

    # Convert to pandas DataFrame
    df = pd.DataFrame(data, columns=['song_name', 'danceability', 'energy', 'loudness', 'popularity', 'liked'])
    return df

# Function to predict song liking (now includes 'popularity' in CSV)
def predict_song_liking(csv_file2):
    new_df = pd.read_csv(csv_file2)

    required_columns = ["danceability", "energy", "loudness", "popularity"]

    if not all(col in new_df.columns for col in required_columns):
        raise ValueError(f"The CSV must contain these columns: {required_columns}")

    # Extract the relevant features for prediction
    features = new_df[required_columns]

    # Use the trained model to predict for each song
    predictions = model.predict(features)

    # Add predictions back into the DataFrame
    new_df['predicted_liked'] = predictions

    # Replace binary values with "Like" or "Dislike"
    new_df['predicted_liked'] = new_df['predicted_liked'].apply(lambda x: "Like" if x == 1 else "Dislike")

    print(predictions)  # This will show the predicted values

    return new_df

# Prompt the user for the CSV file name
csv_file2 = input("Please enter the CSV file name of the playlist to evaluate (with .csv extension): ")

print("Fetching data from database:")
data_from_db = fetch_ml_data()

print(f"\nPredicting song liking from {csv_file2}")
predictions_result = predict_song_liking(csv_file2)
print(predictions_result.head())  # Print the results with predictions

