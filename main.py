# Olly Love
# Movie Rating Processor 
# Project which takes critics ratings from Rotten Tomatoes data
# finds the mode rating and more data, to successfully rate a movie
# results displayed on webpage made with js and react

# Current: work on website portion

from file_handler import FileHandler
from data_processor import DataProcessor

def main():
    fileName = "RTCriticRatingsBatch1.csv"
    outputFileName = "MoviesRated.csv"
    fileHandler = FileHandler(fileName, outputFileName)
    # dictionary of movies with their list of ratings, ie {'Mario': [A+, 1|4, 3|5], 'Wonka': [F, 3|5]...}
    rawData = fileHandler.get_csv_data()
    dataProcessor = DataProcessor(rawData)
    # List of seperate dicts for each movie storing all of their processed stats
    # ie [{'movieTitle': 'Mario', 'numRatings': 20, 'rating': 5,...}, {'movieTitle': 'Oppenheimer', 'numRatings': 1...]
    processedData = dataProcessor.buildOutputDict()
    fileHandler.dataOutput(processedData)
    
if __name__ == "__main__":
    main()

# js then takes this csv file and runs the visualizations - storing or website fetching fancy thing
# can also have page describing rating system w some example games/movies from my rating to give people
# an understanding of the system
# don't need to rerun this python file over and over, once I process the correct data, the site just has it
# this is really more like a helper I can personally use every once in a while if I want a new csv from a new movie

# also once website shows data, think of creating a movie object stored in a csv that goes with the website?
# Each movie object would have something like image, title, director, and MRS (Movie rating stats) object
# w all the movies stats