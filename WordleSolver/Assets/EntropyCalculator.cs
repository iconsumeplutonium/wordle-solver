using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System.Linq;
using System;

public class EntropyCalculator : MonoBehaviour
{
    public GameObject wordInput;
    public GameObject posInput;
    public TMP_Text wordText;
    public TMP_Text posText;
    public GameObject continueButton;

    public List<string> greenLetters;
    public List<string> yellowLetters;
    public List<string> grayLetters;

    public string word;
    public string position;

    public WordFinder wf;


    public void Entropy() {

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

        List<string> wordsThatMatch = wf.FindWords(word, position, grayLetters, yellowLetters, greenLetters);

        Dictionary<string, float> wordValueDict = new Dictionary<string, float>();

        for (int x = 0; x < wordsThatMatch.Count; x++) {
            string word = wordsThatMatch[x];
            float expectedValue = 0;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    for (int k = 0; k < 5; k++) {
                        for (int l = 0; l < 5; l++) {
                            for (int m = 0; m < 5; m++) {

                                string colorCombiation = i.ToString() + j.ToString() + k.ToString() + l.ToString() + m.ToString();

                                if (!isFourGreenOneYellow(colorCombiation)) {
                                    int amountOfWordsThatFit = wf.FindWords(word, colorCombiation, grayLetters, yellowLetters, greenLetters).Count;
                                    if (amountOfWordsThatFit == 0)
                                        continue;

                                    float p = probability(amountOfWordsThatFit, wordsThatMatch.Count);
                                    float info = information(p);

                                    expectedValue += p * info;

                                }
                            }
                        }
                    }
                }
            }

            wordValueDict[wordsThatMatch[x]] = expectedValue;

        }


        string output = "";
        foreach (KeyValuePair<string, float> key in wordValueDict) {
            output += key.Key + ": " + key.Value + ", ";
        }
        Debug.Log(output);


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
        Entropy();

    }

    public void OnContinueButton() {
        wordText.text = "";
        posText.text = "";
        wordInput.SetActive(true);
        continueButton.SetActive(false);
    }

    private float probability(int numWords, int totalWords) {
        return numWords / totalWords;
    }

    private float information(float probability) {
        return Mathf.Log((1 / probability), 2);
    }

    private bool isFourGreenOneYellow(string colors) {
        int total = 0;
        for (int i = 0; i < colors.Length; i++) {
            total += (int)char.GetNumericValue(colors[i]);
        }

        if (total == 6)
            return true;

        return false;

    }
}
