#  Rotten Tomatoes Movie Rating Data Analysis
Data was manually obtained (copied from Rotten Tomatoes and pasted into Excel), cleaned with Excel VBA, and processed in Python.   

Film critics each use their own rating system to decide whether a movie is worth watching. Many online platforms aggregate critic data in different ways in an attempt to give a general concensus on whether a movie is enjoyable or not. I attempt to do the same by normalizing data to a 5 point scale and using the mode as the rating of a movie.

How it Works:
Data is manually obtained by going to the Rotten Tomatoes website and selecting a movie. All of the critic reviews for that movie are copied and pasted into a column of an Excel sheet. 
An Excel VBA script cleans a selected column of data, so that just the ratings remain in that column. Columns are cleaned one at a time.
The cleaned data is manually copied and pasted into a csv file. 
This csv file is read and processed by a Python script.
The Python script normalizes data on a 5 point scale, uses the mode to determine a movies rating, and outputs the data to a csv file.
This csv file displays the movies rating along with many other statistics such as the amount of reviews it got, the amount of each rating, and more.

How to Run:


Future Additions:
More movies + mediums (books, video games)
Website (JS + React) for a user friendly experience. 
Rating comparison with various rating websites to investigate artificial inflation
Note: So far my ratings are mostly in-line with their Rotten Tomatoes counterparts. 
