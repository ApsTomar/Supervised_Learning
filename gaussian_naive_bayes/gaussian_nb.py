import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def load_iris_data():
    data_file = open("iris.csv", 'r')
    reader = list(csv.reader(data_file, delimiter=","))
    n_samples = sum(1 for row in reader)
    n_features = len(reader[0]) - 1
    data = np.empty((n_samples - 1, n_features))
    target = np.empty((n_samples - 1,), dtype=np.int)

    labels = []
    num_of_labels = 0
    index = 0
    for row in reader[1:]:
        data[index] = np.asarray(row[:-1], dtype=np.float)
        if row[-1] in labels:
            # label_value starts from 1
            label_value = labels.index(row[-1]) + 1
        else:
            labels.append(row[-1])
            num_of_labels += 1
            label_value = num_of_labels

        target[index] = np.asarray(label_value, dtype=np.int)
        index += 1

    return data, target


def load_test_data():
    test_data_file = open("test_data.csv", 'r')
    reader = list(csv.reader(test_data_file, delimiter=","))
    n_test_samples = sum(1 for row in reader)
    n_test_features = len(reader[0])
    test_data = np.empty((n_test_samples, n_test_features))
    index = 0
    for row in reader:
        test_data[index] = np.asarray(row, dtype=np.float)
        index += 1

    return test_data


def load_test_labels():
    test_labels_file = open("test_labels.txt", "r")
    test_labels = []
    for row in test_labels_file:
        test_labels.append(np.int(row))

    return test_labels


iris_data, iris_target = load_iris_data()
test_data = load_test_data()
test_labels = load_test_labels()
clf = GaussianNB()
clf.fit(iris_data, iris_target)
pred = clf.predict(test_data)
print accuracy_score(pred, test_labels)
