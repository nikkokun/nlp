# Text Classification

import nltk
import random
from nltk.corpus import movie_reviews


def main():
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]

    # documents = []
    # for category in movie_reviews.categories():
    # 	for fileid in movie_reviews.fileids(category):
    # 		documents.append(list(movie_reviews.words(fileid)), category)

    random.shuffle(documents)  # to prevent extreme bias

    # print(documents[1])

    all_words = []
    for w in movie_reviews.words():
        all_words.append(w.lower()) #we need to convert all words to lower case

    all_words = nltk.FreqDist(all_words)
    print(all_words.most_common(15)) #prints out the 15 most common words
    print("Number of times stupid pops up {}".format(all_words["stupid"]))

if __name__ == '__main__':
    main()
