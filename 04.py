import functools, operator, re

inputFile = open('04_input.txt', 'r')

lineList = [line.replace('\n', '') for line in inputFile]

def getIntListFromString(separator, stringOfNums):
    numStringList = re.split(separator, stringOfNums)
    return [ int(numString.strip()) for numString in numStringList ]

def getElfAndWinningInts(string):
    allNumStrings = re.split(':\W+', string)[1]
    numStringsList = re.split('\W+\|\W+', allNumStrings)
    winingIntList = getIntListFromString('\W+', numStringsList[0])
    elfIntList =    getIntListFromString('\W+', numStringsList[1])
    return elfIntList, winingIntList
    
def isWinningNum(num, list):
    return num in list

def getListOfWinningElfNums(elfNumsList, winningNumsList):
    return [ elfNum for elfNum in elfNumsList if isWinningNum(elfNum, winningNumsList) ] 

# Part 1 Logic
def getElfScore(winningElfNumsList):
    countOfWinningElfNums = len(winningElfNumsList) 
    if countOfWinningElfNums == 0:
        return 0
    else:
        return 2 ** (countOfWinningElfNums - 1)

def getElfScoreFromLine(inputLine):
    elfInts = getElfAndWinningInts(inputLine)[0]
    winningInts = getElfAndWinningInts(inputLine)[1]
    winningElfList = getListOfWinningElfNums(elfInts, winningInts)
    elfScore = getElfScore(winningElfList)
    return elfScore

def getSumOfElfScores(lineList):
    listOfElfScores = [ getElfScoreFromLine(inputLine) for inputLine in lineList]
    return functools.reduce(operator.add, listOfElfScores)

sumOfElfScores = getSumOfElfScores(lineList)

# Part 1 Answer
print(sumOfElfScores)

# Part 2 Logic
def getCountOfWinningElfNums(inputLine):
    elfNumsList = getElfAndWinningInts(inputLine)[0]
    winningNumsList = getElfAndWinningInts(inputLine)[1]
    listOfWinningElfNums = getListOfWinningElfNums(elfNumsList, winningNumsList)
    return len (listOfWinningElfNums)

def getListOfCountsOfWinningElfNums(lineList):
    return [ [getCountOfWinningElfNums(inputLine), 1] for inputLine in lineList ]

def incrementCountOfRangeOfCards(cardScoreAndCountList, cardScoreAndCount, index = 0):

    try:
        countOfWiningNumsOnCurrCard = cardScoreAndCount[0]
        countOfCurrentCards = cardScoreAndCount[1]
        startIncrementIndex = index + 1
        endIncrementIndex = countOfWiningNumsOnCurrCard + index + 1

        for incrementIndex in range(startIncrementIndex, endIncrementIndex):
            cardScoreAndCountList[incrementIndex][1] += countOfCurrentCards
    except IndexError:
        return cardScoreAndCountList
    
    return cardScoreAndCountList

    incrementCountOfRangeOfCards(cardScoreAndCountList, cardScoreAndCount, index + 1)

def getSumOfCardCounts(lineList):
    cardScoreAndCountList = getListOfCountsOfWinningElfNums(lineList)
    for index, cardScoreAndCount in enumerate(cardScoreAndCountList):
        incrementCountOfRangeOfCards(cardScoreAndCountList, cardScoreAndCount, index)
    listOfCardCounts = [ cardScoreAndCount[1] for cardScoreAndCount in cardScoreAndCountList ]
    sumOfCardCounts = functools.reduce(lambda currentCardCount, nextCardCount: currentCardCount + nextCardCount, listOfCardCounts)
    return sumOfCardCounts
    
sumOfCardCounts = getSumOfCardCounts(lineList)

# Part 2 Answer
print(sumOfCardCounts)