import functools, re

inputFile = open('02_input.txt', 'r')

lineList = [line.replace('\n', '') for line in inputFile]

def getTurnList(gameLine):
    turns = gameLine.split(': ')[1]
    turnList = turns.split(';')
    return turnList

def getColorCount(turn, color):
    try:
        colorCount = int(turn.split(f' {color}')[0].split(' ')[-1])
        return colorCount
    except:
        return 0

def getCubeCountByColorDict(turn):
    redCount =      getColorCount(turn, 'red')
    greenCount =    getColorCount(turn, 'green')
    blueCount =     getColorCount(turn, 'blue')

    return {
        'red'   :   redCount,
        'blue'  :   blueCount,
        'green' :   greenCount
    }

def getMaxColorCountDict(currentTurn, nextTurn):
    return {
        'red'   :   currentTurn['red'] if currentTurn['red'] > nextTurn['red'] else nextTurn['red'],
        'green' :   currentTurn['green'] if currentTurn['green'] > nextTurn['green'] else nextTurn['green'],
        'blue'  :   currentTurn['blue'] if currentTurn['blue'] > nextTurn['blue'] else nextTurn['blue']
    }

def getMaxColorCountDictFromList(turnList):
    turnDictList = map(getCubeCountByColorDict, turnList)
    return functools.reduce(getMaxColorCountDict, turnDictList)


# Part 1 Logic
cubeMaxes = {
    'red':      12,
    'green':    13,
    'blue':     14
}

def gameIsPossible(gameLine):
    turnList = getTurnList(gameLine)
    maxColorCountDict = getMaxColorCountDictFromList(turnList)
    redIsPossible = maxColorCountDict['red'] <= cubeMaxes['red']
    greenIsPossible = maxColorCountDict['green'] <= cubeMaxes['green']
    blueIsPossible = maxColorCountDict['blue'] <= cubeMaxes['blue']

    return redIsPossible and greenIsPossible and blueIsPossible

possibleGameList = [ gameIsPossible(gameLine) for gameLine in lineList ]

possibleGameNumberList = [index + 1 for index, gameIsPossible in enumerate(possibleGameList) if gameIsPossible]

sumOfAllPossibleGameNumbers = functools.reduce(lambda currentSum, next: currentSum + next, possibleGameNumberList)

# Part 1 Answer
print(sumOfAllPossibleGameNumbers)

# Part 2 Logic
def getCubeMinimums(gameLine):
    turnList = getTurnList(gameLine)
    maxColorCountDict = getMaxColorCountDictFromList(turnList)
    return maxColorCountDict

def getProductOfCubeMinimums(gameLine):
    cubeMinimums = getCubeMinimums(gameLine)
    return cubeMinimums['red'] * cubeMinimums['green'] * cubeMinimums['blue']

def getSumOfCubeMinimumsProductsList(lineList):
    cubeMinimumsProductList = list(map(getProductOfCubeMinimums, lineList))
    return functools.reduce(lambda current, next: current + next, cubeMinimumsProductList)

sumOfCubeMinimumsProductsList = getSumOfCubeMinimumsProductsList(lineList)

# Part 2 Answer
print(sumOfCubeMinimumsProductsList)