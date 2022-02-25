from wordleList import words


def main(wordInput, posInput, green, yellow, gray):
    wordArr = green
    yellowLetters = yellow
    notInWord = gray

    possibleWords = []
    #possibleWords = 0
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
        #possibleWords += 1      

        
        


    # print("word: " + wordInput + ", posInput: " + posInput)
    # print(wordArr)
    # print(yellowLetters)
    # print(notInWord)
    return possibleWords

    # playAgain = input("Would you like to continue guessing? Y/N")
    # if(playAgain == "y"):
    #     main()

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
    for j in range(len(letterList)):
        if(letterList[j]):
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


# if __name__ == "__main__":
#     main()