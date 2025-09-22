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