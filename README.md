# Wordle Solver

#### Description
Repository name is self explanatory. Inspired by [3Blue1Brown's video](https://www.youtube.com/watch?v=v68zYyaEmEA) about Wordle.

#### Project Files
* brain.py: The original program, designed to simply fetch words matching a given color critera (e.g. 🟩🟨⬛⬛⬛ for "adieu")
* dataGenerator.py: Program to generate probabilities.txt
* entropyCalculator.py: The main program, attempts to solve a given Wordle
* probabilities.txt: Text file containing the number of words that fit all 238 possible color combinations for all 12,971 words
* frequencyData.json: contains word frequency data
* wordfinder.py: brain.py but adapted 
* fullWordleList.py, wordleList.py, wordmasterList.py: lists of words


