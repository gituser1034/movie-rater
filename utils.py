# Olly Love
# Movie Rating Processor - Utilities
# Helper functions aiding in the operations of data processor

import math

class Utils:
    # Takes a string letter rating from A+ to F, converts to numerical scale out of 13
    @staticmethod
    def letterTo13(letterRating):
        letterToNumDict = {
            'A+': 13.0,
            'A': 12.0,
            'A-': 11.0,
            'B+': 10.0,
            'B': 9.0,
            'B-': 8.0,
            'C+': 7.0,
            'C': 6.0,
            'C-': 5.0,
            'D+': 4.0,
            'D': 3.0,
            'D-': 2.0,
            'F': 1.0
        }
        return letterToNumDict[letterRating]
    
    # Takes a number and returns its word counterpart, ie 4 = Great
    @staticmethod
    def numRatingToWord(num):
        numToWordDict = {
            5: "Amazing",
            4: "Great",
            3: "Ok",
            2: "Bad",
            1: "Terrible"
        }
        return numToWordDict[num]
    
    # Takes a number, rounds it properly based on .5 being rounded to next whole number
    # returns correctly rounded number
    @staticmethod
    def properRounding(num):
        # ie 4.5 / 1, 1 goes into 4.5 4 times, w .5 as a remainder, 4.5 / 1 = 4.5
        if num % 1 >= 0.5:
            result = math.ceil(num)
        else:
            result = math.floor(num)

        return result