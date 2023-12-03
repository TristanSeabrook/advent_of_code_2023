import functools, re
from itertools import chain

inputFile = open('03_input.txt', 'r')

lineList = [line.replace('\n', '') for line in inputFile]

def getCharAt(x, y, inputList):
    try:
        return inputList[y][x]
    except IndexError:
        return ''

def getAdjacentChars(x, y, inputList):
    coordsToCheck = [
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)
    ]
    
    adjacentCharList = [ getCharAt(coords[0], coords[1], inputList) for coords in coordsToCheck]

    return adjacentCharList

def getMatchDict(search, lineNumber):
    matchDict = {
        'match': search.group(),
        'start' : search.start(),
        'end'   : search.end(),
        'line'  : lineNumber
    }
    return matchDict

def getDictsOfMatchesInString(string, regex, lineNumber):
    reSearch = re.finditer(regex, string)
    startAndEndList = [ getMatchDict(match, lineNumber) for match in reSearch ]
    return startAndEndList

# Part 1 Logic
def getDictsOfAllNumbersInList(inputList):
    numberRegex = r'\d+'
    return [getDictsOfMatchesInString(string, numberRegex, index) for index, string in enumerate(inputList)]

def getAllCharsAdjacentToNumber(matchDict, inputList):
    y = matchDict['line']
    xStart = matchDict['start']
    xEnd = matchDict['end']

    allAdjacentChars = [ getAdjacentChars(x, y, inputList) for x in range(xStart, xEnd) ]
    
    return allAdjacentChars

def isSymbol(char):
    return re.match('((?=[^.])\D)', char) != None

def isAdjacentToSymbol(listsOfAdjacentChars):
    for listOfAdjacentChars in listsOfAdjacentChars:
        if any(isSymbol(char) for char in listOfAdjacentChars):
            return True
    return False

def getListOfDictsOfAllNumbersInList(inputList):
    return list(chain.from_iterable(getDictsOfAllNumbersInList(inputList)))

def sumAllNumbersAdjacentToSymbols(inputList):
    dictsOfAllNumbersInList = getListOfDictsOfAllNumbersInList(inputList)

    sumOfAllNumbersAdjacentToSymbols = 0

    for matchDict in dictsOfAllNumbersInList:
        adjacentChars = getAllCharsAdjacentToNumber(matchDict, inputList)
        if isAdjacentToSymbol(adjacentChars):
            sumOfAllNumbersAdjacentToSymbols += int(matchDict['match'])
    
    return sumOfAllNumbersAdjacentToSymbols

sumOfAllNumbersAdjacentToSymbols = sumAllNumbersAdjacentToSymbols(lineList)

# Part 1 Answer
print(sumOfAllNumbersAdjacentToSymbols)

# Part 2 Logic
def getDictsOfAllPotentialGearsInList(inputList):
    gearRegex = '\*'
    return [getDictsOfMatchesInString(string, gearRegex, index) for index, string in enumerate(inputList)]

def isAdjacentToExactlyTwoNumbers(x, y, inputList):
    adjacentCharList = getAdjacentChars(x, y, inputList)
    topChars = ''.join(adjacentCharList[5:])
    leftChar = adjacentCharList[3]
    rightChar =  adjacentCharList[4]
    bottomChars = ''.join(adjacentCharList[0:3])
    searchString = f'{topChars}|{leftChar}|{rightChar}|{bottomChars}'
    matches = [match for match in re.finditer('\d+', searchString)]
    return len(matches) == 2

def getListOfPotentialGearDicts(inputList):
    dictsOfAllPotentialGearsInList = list(chain.from_iterable(getDictsOfAllPotentialGearsInList(lineList)))
    return dictsOfAllPotentialGearsInList

def gearFilter(gearDict):
    x = gearDict['start']
    y = gearDict['line']
    return isAdjacentToExactlyTwoNumbers(x, y, lineList)

def numberIsAdjacent(x, y):
    
    def adjacentNumbersFilter(numberDict):
        numberXStart = numberDict['start']
        numberXEnd = numberDict['end']
        numberY = numberDict['line']
        adjacentY = abs(y - numberY) <= 1 
        adjacentX = numberXStart - 1 <= x < numberXEnd + 1
        return adjacentX and adjacentY

    return adjacentNumbersFilter

def getSumOfAllGearRatios(inputList):
    potentailGearDictList = getListOfPotentialGearDicts(inputList)
    gearDictList = [gearDict for gearDict in filter(gearFilter, potentailGearDictList)]
    numberDictList = getListOfDictsOfAllNumbersInList(inputList)

    gearRatioSum = 0

    for gearDict in gearDictList:
        x = gearDict['start']
        y = gearDict['line']
        adjacentNumbersFilter = numberIsAdjacent(x, y)
        adjacentNumbers = [int(numberDict['match']) for numberDict in filter(adjacentNumbersFilter, numberDictList)]
        gearRatio = adjacentNumbers[0] * adjacentNumbers[1]
        gearRatioSum += gearRatio
    
    return gearRatioSum

sumOfAllGearRatios = getSumOfAllGearRatios(lineList)
        
# Part 2 Answer 
print(sumOfAllGearRatios)