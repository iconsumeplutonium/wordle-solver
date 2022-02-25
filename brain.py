# input word
# input 12312 whcih tells you gree/yellow/gray
from fullWordleList import words



wordArr = []
yellowLetters = [] #string array where yellow letters are stored as "r2" to show that r is yellow in spot 2
notInWord = []

def main():

    wordInput = input("input the word: ")
    while(len(wordInput) != 5): #should check for is all ltters here :)
            wordInput = input("input the word: ")
    
    posInput = input("input positions: ")
    while(len(posInput) != 5 or not posInput.isdecimal):
            posInput = input("input positions: ")

    # assign letters to proper arrays
    for i in range(5):
        if(int(posInput[i]) == 1):
            letter = str(wordInput[i] + str(i))
            if(letter not in wordArr):
                wordArr.append(letter)

        elif(int(posInput[i]) == 2):
            letter = str(wordInput[i] + str(i))
            if(letter not in yellowLetters):    
                yellowLetters.append(str(wordInput[i] + str(i)))

        elif(int(posInput[i]) == 3):
            num = wordInput.count(wordInput[i])
            if(num == 1 and wordInput[i] not in notInWord):
                notInWord.append(wordInput[i])
            else:
                letter = str(wordInput[i] + str(i))
                if(letter not in notInWord):
                    notInWord.append(letter)

    possibleWords = []
    for i in range(len(words)):
        #check if banned letter is in word
        if(containsBannedLetters(notInWord, words[i])):
            continue
        
        #if yellow letter not in word/in not spot its supposed to be
        if(containsYellowLetterInBannedPos(yellowLetters, words[i])):
            continue
    
        if(containsGreenLetterInIncorrectPos(wordArr, words[i])):
            continue

        possibleWords.append(words[i])



        

        
        


    # print("word: " + wordInput + ", posInput: " + posInput)
    print(wordArr)
    print(yellowLetters)
    print(notInWord)
    print(possibleWords)

    playAgain = input("Would you like to continue guessing? Y/N")
    if(playAgain == "y"):
        main()

# returns true if a banned letter is in a word
def containsBannedLetters(letterList, word):
    for j in range(len(letterList)):
        if(len(letterList[j]) > 1):
            letter = letterList[j][0]
            pos = int(letterList[j][1])
            if(letter in word[pos]):
                return True
        else:
            if(letterList[j] in word):
                return True

    return False

# returns true if the letter isnt in the word or if the letter is in a spot it shoulnt be
def containsYellowLetterInBannedPos(letterList, word):
    contains = False
    for j in range(len(letterList)): # if this breaks, add an "if(letterlist[j])" here
        letter = letterList[j][0]
        pos = int(letterList[j][1])
        if(letter in word):
            if(letter in word[pos]):
                contains = True
        else:
            contains = True
    
    return contains

def containsGreenLetterInIncorrectPos(letterList, word):
    for j in range(len(letterList)):
#        if((letterList[j] != None) and (letterList[j] in word) and (letterList[j] != word[j])):
        if(letterList[j]):
            letter = letterList[j][0]
            pos = int(letterList[j][1])
            if(letter in word):
                if (not (letter in word[pos])):
                    return True
            else:
                return True

    return False


if __name__ == "__main__":
    main()