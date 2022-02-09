using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using UnityEngine.UI;
using TMPro;

public class WordFinder : MonoBehaviour {

    public List<string> greenLetters;
    public List<string> yellowLetters;
    public List<string> grayLetters;

    public string word;
    public string position;

    private bool hasTypedWord;

    public GameObject wordInput;
    public GameObject posInput;
    public TMP_Text wordText;
    public TMP_Text posText;
    public GameObject continueButton;

    private void Start() {

    }

    public void main() {
        if (word != null && position != null) {
            for (int i = 0; i < 5; i++) {

                int number = (int)char.GetNumericValue(position[i]);
                switch (number) {
                    case 1:
                        string letter = word[i].ToString() + i;
                        if (!greenLetters.Contains(letter))
                            greenLetters.Add(letter);
                        break;

                    case 2:
                        string letter1 = word[i].ToString() + i;
                        if (!yellowLetters.Contains(letter1))
                            yellowLetters.Add(letter1);
                        break;

                    default:
                        int letterCount = word.Count(c => c == word[i]);
                        //Debug.Log(word[i] + " " + letterCount);
                        if (letterCount == 1) //&& !grayLetters.Contains(word[i].ToString())) //doesnt account for it already being there as a letter + index
                            grayLetters.Add(word[i].ToString());
                        else {
                            string letter3 = word[i].ToString() + i;
                            if (!grayLetters.Contains(word[i].ToString())) //clean up this mess
                                grayLetters.Add(word[i].ToString() + i);
                        }

                        break;
                }
            }

            List<string> possibleWords = new List<string>();
            for (int i = 0; i < WordmasterList.words.Count; i++) {
                if (containsGrayLetters(grayLetters, WordmasterList.words[i]))
                    continue;

                if (containsYellowLetters(yellowLetters, WordmasterList.words[i]))
                    continue;

                if (containsGreenLetters(greenLetters, WordmasterList.words[i]))
                    continue;

                possibleWords.Add(WordmasterList.words[i]);
            }

            string output = "";
            foreach (var w in possibleWords) {
                output += w + ", ";
            }
            Debug.Log(output);

            continueButton.SetActive(true);

        } 
    }

    /*
     * if the length of the gray letter string is 2, that means it is a letter and a position
        it checks if the letter is in that position in the word. If so, it returns true.

        if the letter of the gray letter is 1, it checks if the letter is in the word and returns true if it does contain it. 
    */
    private bool containsGrayLetters(List<string> grayLetters, string word) {
        for (int i = 0; i < grayLetters.Count; i++) {
            if(grayLetters[i].Length > 1) {
                char letter = grayLetters[i][0];
                int pos = (int)char.GetNumericValue(grayLetters[i][1]);
                if(word[pos] == letter)
                    return true;
            } else {
                if (word.Contains(grayLetters[i]))
                    return true;
            }
        }
        
        return false;
    }
    
    /*
     * each yellow letter array element is a letter plus a position index 
     * first we check if the letter is even in the word. if not, we return true
     * if it is in the word, we check if its in that position index. if it is, we return true as well. 
     */
    private bool containsYellowLetters(List<string> yellowLetters, string word) {
        for (int i = 0; i < yellowLetters.Count; i++) {
            char letter = yellowLetters[i][0];
            int pos = (int)char.GetNumericValue(yellowLetters[i][1]);
            if (word.Contains(letter)) {
                //Debug.Log(pos);
                if (word[pos] == letter)
                    return true;
            } else
                return true;
        }
        
        
        return false;
    }

    /*
     * each green letter array is a letter plus a pos index
     * first we check if the letter is even in the word. if not, return true
     * then we check if the ltter is in the correct spot. if not, return true. 
     */
    private bool containsGreenLetters(List<string> greenLetters, string word) {
        for (int i = 0; i < greenLetters.Count; i++) {
            char letter = greenLetters[i][0];
            int pos = (int)char.GetNumericValue(greenLetters[i][1]);
            if (word.Contains(letter)) {
                if (!(word[pos] == letter))
                    return true;
            }
            else
                return true;
        }
        
        return false;
    }

    public void OnWordInputEntered(TMP_InputField input) {
        word = input.text;
        input.text = "";
        wordInput.SetActive(false);
        posInput.SetActive(true);
        wordText.text = word;
    }

    public void OnPositionInputEntered(TMP_InputField input) {
        position = input.text;
        input.text = "";
        posInput.SetActive(false);
        posText.text = position;
        main();

    }

    public void OnContinueButton() {
        wordText.text = "";
        posText.text = "";
        wordInput.SetActive(true);
        continueButton.SetActive(false);
    }
}
