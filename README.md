#  Rotten Tomatoes Movie Rating Data Analysis
Author: Olly Love

Film critics each use their own rating system to decide whether a movie is worth watching. Many online platforms aggregate critic data in different ways in an attempt to give a general concensus on whether a movie is enjoyable or not. I attempt to do the same by normalizing data to a 5 point scale and using the mode as the rating of a movie.

Tools Used: Excel VBA, Python

# How it Works:
- Data is manually obtained through Rotten Tomatoes. All of the critic reviews for a chosen movie are copied and pasted into a column of an Excel sheet. 
- An Excel VBA script cleans a selected column of data, so that just the ratings remain in that column.
- The cleaned data is manually copied and pasted into a csv file. 
- This csv file is read and processed by a Python script.
- The Python script normalizes data on a 5 point scale, uses the mode to determine a movies rating, and outputs the data to a csv file.
- This csv file displays the movies rating along with many other stats.

# How to Run:
- Clone this repo.
- Go to Rotten Tomatoes, choose a movie you like, copy and paste the critic reviews into a column in the xlsm file.
- Select and clean the column via the clean button.
- Empty the previous data from the input csv file (leave the title and headers), then copy and paste the cleaned data into a column here. 
- Run main.py

# Future Additions:
Website (JS + React) for a user friendly experience. 
Rating comparison with various rating websites to investigate artificial inflation.
Note: So far my ratings are mostly in-line with their Rotten Tomatoes counterparts. 
More movies + mediums (books, video games).
