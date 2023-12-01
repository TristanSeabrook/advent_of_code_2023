import functools, re

inputFile = open('01_input.txt', 'r')

lineList = [line.replace('\n', '') for line in inputFile]

def getFirstNumber(line):
    return re.findall('\d', line)[0]

def getLastNumber(line):
    return re.findall('\d', line)[-1]

def getTwoDigitNumber(line):
    return(int(f'{getFirstNumber(line)}{getLastNumber(line)}'))

def getTwoDigitList(list):
    return [getTwoDigitNumber(line) for line in list]

def getSumOfTwoDigitList(list):
    return functools.reduce(lambda sum, next: sum + next, list)

# Part 1 Logic
twoDigitList = getTwoDigitList(lineList)

sumOfTwoDigitList = getSumOfTwoDigitList(twoDigitList)

# Part 1 Answer
print(sumOfTwoDigitList)

# Part 2 Logic
digitDict = {
    'one':      'o1e',
    'two':      't2o',
    'three':    't3e',
    'four':     'f4r',
    'five':     'f5e',
    'six':      's6x',
    'seven':    's7n',
    'eight':    'e8t',
    'nine':     'n9e'
}

digitDictKeyList = list(digitDict.keys())

def replaceStringsWithDigits(inputString, keyList, inputDict, iteration = 0):
    endOfList = len(keyList)
    if iteration == endOfList:
        return inputString 
    else:
        currentKey = keyList[iteration]
        nextIteration = iteration + 1
        updatedString = inputString.replace(currentKey, inputDict[currentKey])
        return replaceStringsWithDigits(updatedString, keyList, inputDict, nextIteration)


replacedLineList = [replaceStringsWithDigits(line, digitDictKeyList, digitDict) for line in lineList]

twoDigitReplacedLineList = getTwoDigitList(replacedLineList)

sumOfTwoDigitReplacedLineList = getSumOfTwoDigitList(twoDigitReplacedLineList)

# Part 2 Answer
print(sumOfTwoDigitReplacedLineList)
















