import numpy as np
from matplotlib import pyplot as plt


def main():
    dracula()
    bikes()
    random_data_2d()
    random_data_3d()


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


def random_data_2d():
    no_of_clusters = 3
    cluster_mean = np.random.rand(no_of_clusters, 2)

    data = np.array([[]])
    target = np.array([[]], dtype='int')

    points_per_cluster = 100
    sigma = 0.1
    for i in range(no_of_clusters):
        noise = sigma * np.random.randn(points_per_cluster, 2)
        cluster = cluster_mean[i, :] + noise
        data = np.append(data, cluster).reshape((i + 1) * points_per_cluster, 2)
        target = np.append(target, [i] * points_per_cluster)

    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], c=target)
    plt.show()
    return


def random_data_3d():
    no_of_clusters = 3
    cluster_mean = np.random.rand(no_of_clusters, 3)

    data = np.array([[]])
    target = np.array([[]], dtype='int')

    points_per_cluster = 100
    sigma = 0.1
    for i in range(no_of_clusters):
        noise = sigma * np.random.randn(points_per_cluster, 3)
        cluster = cluster_mean[i, :] + noise
        data = np.append(data, cluster).reshape((i + 1) * points_per_cluster, 3)
        target = np.append(target, [i] * points_per_cluster)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=target)
    plt.show()
    return


main()

