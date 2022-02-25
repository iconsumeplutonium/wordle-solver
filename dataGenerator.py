import time
import wordfinder
from fullWordleList import words
import math

def probability(words, totalWords):
    return round(float(words / totalWords), 2)

def information(probability):
    return math.log2(1 / probability)



with open("probabilities.txt", 'a') as file:

    # for word in words:
    #     if(word.index(word) > 0):
    #         break
    start = time.time()
    for x in range(421, 12971):
        line = words[x] + " "
        for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            for m in range(3):
                                if((i + j + k + l + m) == 0):
                                    p = 0.0001 #round(1 / 12971, 4)
                                else:
                                    colorCombination = str(i + 1) + str(j + 1) + str(k + 1) + str(l + 1) + str(m + 1)
                                    amountOfWordsThatFit = wordfinder.main(words[x], colorCombination, [], [], [])
                                    p = round(amountOfWordsThatFit / 12971, 4)              

                                line += str(p) + " "
        line += "\n"
        file.write(line)
        print("completed " + str(x + 1) + "/12971")

    end = time.time()

    print(str(end - start))



    file.close()
