#!/usr/bin/env python3
# Created by nicoroble on 2018/07/11
# Naive Bayse Algorithm

import nltk
import random
from nltk.corpus import movie_reviews
import pickle


def find_features(document, word_features):
    words = set(document)
    features = {}

    for w in word_features:
        features[w] = (w in words)

    return features


def main():
    global documents
    global all_words # contains all the words in movie reviews
    global word_features  # list containing all the word features
    global featuresets
    global training_set
    global testing_set

    documents = [(list(movie_reviews.words(fileid)), category)  # [(review, category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    all_words = []

    # documents = []
    # for category in movie_reviews.categories():
    # 	for fileid in movie_reviews.fileids(category):
    # 		documents.append(list(movie_reviews.words(fileid)), category)

    random.shuffle(documents)  # to prevent extreme bias

    # print(documents[1])

    for w in movie_reviews.words():
        all_words.append(w.lower())  # we need to convert all words to lower case

    all_words = nltk.FreqDist(all_words)
    word_features = list(all_words.keys())[:3000]  # top 3000 words

    # print(all_words.most_common(15))  # prints out the 15 most common words
    # print("Number of times stupid pops up {}".format(all_words["stupid"]))
    # print((find_features(movie_reviews.words('neg/cv000_29416.txt'), word_features)))
    featuresets = [(find_features(rev, word_features), category) for (rev, category) in documents]

    training_set = featuresets[:1900]
    testing_set = featuresets[1900:]

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Naive Bayes Algorithm accuracy: ", (nltk.classify.accuracy(classifier, testing_set)) * 100)
    classifier.show_most_informative_features(15)

    # save_classifier = open("naivebayes.pickle", "wb")
    # pickle.dump(classifier, save_classifier)
    # save_classifier.close()

    classifier_f = open("naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    print("Naive Bayes Algorithm accuracy: ", (nltk.classify.accuracy(classifier, testing_set)) * 100)
    classifier_f.close()

if __name__ == '__main__':
    main()
