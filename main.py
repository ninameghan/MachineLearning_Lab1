import numpy as np


def main():
    dracula()


def dracula():
    minWordLength = 5
    minWordOccurence = 300
    wordOccurences = {}

    # open the file
    file_obj = open("data/Dracula.txt", "r")

    # read data from file
    file_data = file_obj.read()
    file_obj.close()

    # split words
    words = file_data.split()

    for word in words:
        if len(word) >= minWordLength:
            if word in wordOccurences:
                wordOccurences[word] = wordOccurences[word] + 1
            else:
                wordOccurences[word] = 1

    for word in wordOccurences:
        if wordOccurences[word] >= minWordOccurence:
            print(word + ":" + str(wordOccurences[word]))
    return




main()

