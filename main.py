import numpy as np


def main():
    dracula()
    bikes()


def dracula():
    minWordLength = 5
    minWordOccurence = 300
    wordOccurences = {}

    # open the file
    file = open("data/Dracula.txt", "r")

    # read data from file
    data = file.read()
    file.close()

    # split words
    words = data.split()

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


def bikes():
    file = open("data/day.csv", "r")
    weather = np.array([], dtype=int)
    rentals = np.array([], dtype=int)

    for line in file:
        elements = line.split(",")
        if elements[0] != "instant":
            weather = np.append(weather, int(elements[8]))
            rentals = np.append(rentals, int(elements[15]))

    file.close()

    print("Number of days: ", np.sum(weather == 1))
    print("Average number of rentals: ", np.mean(rentals[weather == 1]))

    return


main()

