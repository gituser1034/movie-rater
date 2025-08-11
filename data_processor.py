# Olly Love
# Movie Rating Processor - DataProcessor Class
# Cleans and normalizes passed in data to send back to 
# file handler to be written to csv

import re
from utils import Utils

# Cleans and processes data read in by file handler
class DataProcessor:
    def __init__(self, rawData):
        self.rawData = rawData

    # Takes list of unprocessed ratings for a movie 
    # returns list of ratings normalised on a scale from 1-5
    # Processes letter ratings (converted to scale of 13 then normalized) 
    # and numerical ratings while ignoring potential garbage values
    def normalize5(self, ratings):
        ratings5 = []

        for rating in ratings:
            dataSplit = rating.split('|')
            match = re.search(r'^[A-F][+-]?$', dataSplit[0])
            if match:
                dataSplit[0] = Utils.letterTo13(dataSplit[0])
                # ie 10/13, 13/2.6 = 5, so divide numerator accordingly too
                normalized = dataSplit[0] / 2.6
            # When not letter rating should be form ie "1|4" or "2|2", split has 2 values 
            # length check avoids errored ratings of ie just 7 instead 7/10 or a phrase like "good"
            elif len(dataSplit) == 2:
                try:
                    dataSplit[0] = float(dataSplit[0])
                    dataSplit[1] = float(dataSplit[1])
                except ValueError:
                    continue

                # ie 11/10, give a 5
                if dataSplit[0] > dataSplit[1]:
                    ratings5.append(5)
                    continue

                # dividing 5 by denom gets a number that we multiply numerator by for conversion
                toMulBy = 5.0 / dataSplit[1]
                normalized = dataSplit[0] * toMulBy
            else:
                continue

            if normalized < 1:
                ratings5.append(1)
            # Whole numbers no decimal values, ie 3 % 1 = 0, 1 fits into 3 perfectly no leftovers
            elif normalized % 1 == 0:
                ratings5.append(int(normalized))
            else:
                ratings5.append(Utils.properRounding(normalized))            
        
        return ratings5

    # gets amount of 1 star, 2 star, 5 star, etc
    def getRatingAmounts(self, ratings):
        ratingsDict = {1:0, 2:0, 3:0, 4:0, 5:0}
        for rating in ratings:
            ratingsDict[rating] += 1

        return ratingsDict

    # instead of passing dict {1: 10, 2: 34, ...} pass in amount of ie 1 ratings (n), along w numRatings
    # for ie 10 / 235 = something
    def getFractionAndPercentage(self, value, totalRatings):
        frac = str(value) + '/' + str(totalRatings)
        perc = str(Utils.properRounding((value/totalRatings)*100)) + '%'
        return frac, perc

    # Takes dictionary of ratings, the most popular rating (mode) is the overall rating
    # also gets the word rating, ie 4 = Great, 5 = Amazing
    def getOverallRatings(self, ratingsDict):
        # Get largest amount of ratings, then find the rating (key) associated with it
        maxRatingsAmount = max(ratingsDict.values())
        for key, value in ratingsDict.items():
            if value == maxRatingsAmount:
                overallNumRating = key
                break

        overallWordRating = Utils.numRatingToWord(overallNumRating)

        return overallNumRating, overallWordRating

    # Uses dict of raw movie data ie {'Mario': [A+, 1|4, 3|5], 'Wonka': [F, 3|5]...}
    # Returns a list of dictionaries storing the data of each movie
    # Goes through each movie, calls processing functions on each list of ratings
    # like normalize to get on a scale of 5, get the overall rating based on mode of ratings given
    def buildOutputDict(self):
        outputDict = {}
        outputDicts = []
        # will store like {1: 5, 2: 30, 3: 102} showing ie there are 102 3 star ratings
        ratingsDict = {}
        normalizedRatings = []
        totalRatings = 0

        for movieKey, ratings in self.rawData.items():
            outputDict["movieTitle"] = movieKey
            totalRatings = len(ratings)
            outputDict["numRatings"] = totalRatings

            normalizedRatings = self.normalize5(ratings)
            ratingsDict = self.getRatingAmounts(normalizedRatings)

            overallNumRating, overallWordRating = self.getOverallRatings(ratingsDict)
            outputDict["rating"] = overallNumRating
            outputDict["wordRating"] = overallWordRating

            # Building fraction and percentage part of dict from 1 to 5 stars
            for i in range(1,6):
                # check this function
                frac, perc = self.getFractionAndPercentage(ratingsDict[i], totalRatings)
                # ex. outputDict["1Star"] = ratingsDict[1]
                outputDict[str(i) + "Star"] = ratingsDict[i]
                outputDict[str(i) + "Frac"] = frac
                outputDict[str(i) + "Perc"] = perc

            outputDicts.append(outputDict)
            outputDict = {}

        return outputDicts

