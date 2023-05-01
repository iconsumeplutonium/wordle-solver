from operator import itemgetter
import wordfinder
import math
from fullWordleList import words
import json

def probability(words, totalWords):
    return round(float(words / (totalWords)), 2)

def information(probability):
    return math.log2(1 / probability)

def sigmoid(x):
    return 1 / (1 + math.exp(-1 * x))

greenLetters = []
yellowLetters = []
grayLetters = []

global currentGuess


def main():
    #region input stuff
    wordInput = input("input the word: ")
    while(len(wordInput) != 5 or not wordInput.isalpha): 
            wordInput = input("input the word: ")
    
    posInput = input("input positions: ")
    while(len(posInput) != 5 or not posInput.isdecimal):
            posInput = input("input positions: ")

    # assign letters to proper arrays
    for i in range(5):
        if(int(posInput[i]) == 1):
            letter = str(wordInput[i] + str(i))
            if(letter not in greenLetters):
                greenLetters.append(letter)

        elif(int(posInput[i]) == 2):
            letter = str(wordInput[i] + str(i))
            if(letter not in yellowLetters):
                yellowLetters.append(str(wordInput[i] + str(i)))

        elif(int(posInput[i]) == 3):
            num = wordInput.count(wordInput[i])
            if(num == 1): # and wordInput[i] not in grayLetters):
                grayLetters.append(wordInput[i])
            else:
                letter = str(wordInput[i] + str(i))
                if(letter not in grayLetters):
                    grayLetters.append(letter)


    #endregion

    # Find which words match the criteria
    wordsThatMatch = wordfinder.main(wordInput, posInput, greenLetters, yellowLetters, grayLetters)

    wordValueDict = {}
    with open("probabilities.txt", 'r') as file:

        # prepare the probabilities and word frequency file for reading
        content = file.readlines()
        f = open('frequencyData.json')
        freqData = json.load(f)

        for word in wordsThatMatch:
            # the index of the word in the word array is the line its on in the text file
            index = words.index(word)   
            probabilitiesFromFile = content[index]

            probabilitiesFromTxtFile = probabilitiesFromFile.split()
            expectedValue = 0

            # we only want to get the probabilities of possible colorCombos in which the greens match up
            # check to see which positions of the word has a green letter
            # we loop through the combinations of colors that dont have a green letter
            # eg if the colors are 1xx1x, then we only loop through the 2nd, 3rd, and 5th letters to get the probabilities of those words
            i_range = 1 if isInGreenLetters(0, greenLetters) else 3
            j_range = 1 if isInGreenLetters(1, greenLetters) else 3
            k_range = 1 if isInGreenLetters(2, greenLetters) else 3
            l_range = 1 if isInGreenLetters(3, greenLetters) else 3
            m_range = 1 if isInGreenLetters(4, greenLetters) else 3
            indexesToCheck = []

            for i in range(i_range):
                for j in range(j_range):
                    for k in range(k_range):
                        for l in range(l_range):
                            for m in range(m_range):
                                indexesToCheck.append((i * 3) + (j * 3) + (k * 3) + (l * 3) + (m * 3))


            # find the expected value of the word
            # sum of each probability times each expected value
            for i in range(len(probabilitiesFromTxtFile)):
                if(i == 0):
                    continue

                if(i in indexesToCheck):
                    p = (round((float(probabilitiesFromTxtFile[i]) * 12971)) / len(wordsThatMatch))

                    if(p > 0):
                        info = information(p)
                        expectedValue += p * info
                
            # calculate its final score using random math and word frequency data
            freq = sigmoid(freqData[word])
            global currentGuess
            wordValueDict[word] = round((freq * (currentGuess + 1)) + (1 - freq) * (currentGuess + 1 + expectedValue), 8)

    # create a dictionary with the frequency data of only the words that match
    wordFreqDict = {}
    for key in wordValueDict:
        wordFreqDict[key] = freqData[key]

   
    # sort predictions by word frequency if the score is greater than 5 or we're on the 3rd guess
    # otherwise, sort by score
    if(len(wordValueDict) == 0):
        print("ERROR: NO WORDS MATCH")
        exit()

    print("-------------------------------")
    print("WORD     SCORE           FREQ")
    print("-------------------------------")
    chosenDictionary = wordFreqDict if ((currentGuess > 2) or (averageValue(wordValueDict) > 5)) else wordValueDict

    # remove any words with multiple letters on the first and 2nd guess, or words with a frequency less than 0.00003
    chosenDictionaryCopy = dict(chosenDictionary) #create a copy 
    if(currentGuess <= 2):
        for key, value in sorted(chosenDictionary.items(), key = itemgetter(0), reverse = True):
            s = set(key)
            if(len(s) < 4 or chosenDictionary[key] < 0.000003):
                del chosenDictionary[key]


    # for some reason on random words it will, for no apparent reason whatsoever, delete every single key in the dictionary
    #even if len(s) >= 4 and chosenDict[key] >= 0.000003. This forces it to keep the dictionary populated anyways. Thank you python, very cool.
    chosenDictionary = chosenDictionaryCopy if chosenDictionary == {} else chosenDictionary

    # print the words
    index = 0
    for key, value in sorted(chosenDictionary.items(), key = itemgetter(1), reverse = True):
        if(index > 20):
            break
        
        print(key, "  ", value, "    ", freqData[key])
        index += 1
    
    playAgain = input("Would you like to continue guessing? Y/N")
    if(playAgain == "y"):
        currentGuess += 1
        print("\n")
        main()


def isFourGreenOneYellow(colors):
    total = 0
    for i in range(5):
        total += int(colors[i])
    
    if(total == 6):
        return True
    
    return False

# returns true if a letter is in the green letters array, false otherwise
def isInGreenLetters(index, greenLetters):
    for i in range(len(greenLetters)):
        if(int(greenLetters[i][1]) == index):
            return True
    
    return False

def averageValue(dict):
    totalValue = 0
    for value in dict:
        totalValue += int(dict[value])
    
    return totalValue / len(dict)

#formula to convert 11333 or whatever into array index
# i * 3 + j * 3 + k * 3 + l * 3 + m * 3

if __name__ == "__main__":
    currentGuess = 1
    main()


