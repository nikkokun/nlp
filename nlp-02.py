# STOP WORDS
# !/anaconda/bin/python python 3

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."


def main():
    # main code here
    stop_words = set(stopwords.words("english"))
    print(stop_words)
    words = word_tokenize(example_sentence)
    print(words)
    # long method below
    # filtered_sentence = []
    # for word in words:
    # 	if word not in stop_words:
    # 		filtered_sentence.append(word)

    filtered_sentence = [word for word in words if not word in stop_words]

    print('\t')
    print(filtered_sentence)


if __name__ == "__main__":
    # main execution
    main()
