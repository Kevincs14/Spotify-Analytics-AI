
# Predictify: Spotify Song Predictor
Hey, my name is Kevin Armenteros! Im big into music and lately, I've been really into house music. There are so many undiscovered songs and albums coming out all the time that I don’t have the time—or frankly the patience—to sit and listen to everything. So, I took inspiration from how Spotify recommends music to listeners and thought, why not make something where I can throw in a random house music playlist and get an accurate prediction of what songs I would like? This way, I can spend less time on songs I don't enjoy and focus on discovering the ones I love.

This project uses machine learning to predict whether you will like a song based on audio features such as danceability, energy, loudness, and popularity. It’s a fun way to automate playlist curation and make sure you’re always finding new tracks so you dont play the same song in your car everyday.

## Getting Started:
### export a playlist from Spotify using the Exportify tool. The CSV file you download will need to contain the following columns:

danceability,
energy,
loudness,
popularity, and
liked 

two example csv files are provided in files to help with what your csv file should look likes

After exporting, make sure the liked column accurately reflects which songs you enjoy (1 for liked, 0 for disliked). This data will train the model to predict song preferences based on audio features.

This Python project uses a logistic regression model to predict whether or not you’ll like each song based on its audio features. To use it:

Clone this repository or download the Python script (spotify.py).

Install the necessary Python packages:
bash
Copy code
pip install pandas scikit-learn sqlite3
Run the script to load your playlist CSV and predict which songs you’ll like.
Predict Song Likes:
The script will predict whether you’ll like each song based on the data in your CSV file. This means the model will sort out songs you won’t enjoy, saving you time and letting you focus on songs that fit your taste.

## How to Use
### Exportify CSV Export:
Go to Exportify, sign in to Spotify, and export your playlist as a CSV file.
Ensure that your CSV includes the necessary columns (song_name, danceability, energy, loudness, popularity, liked).
Download the CSV file and save it to your project folder.
Run the Code:
Clone this repository or download the Python script.
Install the required dependencies (as mentioned earlier).
Run the script, and the program will process your playlist and predict which songs you will like.
View Results:
Once the model runs, the script will show you the songs you're most likely to enjoy, based on the predictions made by the logistic regression model.

## Conclusion
While this project is far from finished, it’s already a pretty cool and functional tool. The ultimate goal, however, is to turn this into a fully-fledged website. In the future, I plan to make it easy for users to directly upload their playlists, and the system will not only predict which songs they will like but also display the results in a saved playlist of songs the AI thinks you will like. However due to school and work, I haven't been able to complete the site yet. But stay tuned—expect the full, fully functional version in the near future!

Feel free to open an issue or submit a pull request if you'd like to contribute, or if you have any questions, constructive feedback, or comments!

Happy listening!
