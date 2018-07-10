# LEMMATIZING
# !/anaconda/bin/python python 3

from nltk.stem import WordNetLemmatizer


def main():
    # main code here
    lemmatizer = WordNetLemmatizer()
    print(lemmatizer.lemmatize("cats"))
    print(lemmatizer.lemmatize("cacti"))
    print(lemmatizer.lemmatize("geese"))
    print(lemmatizer.lemmatize("rocks"))
    print(lemmatizer.lemmatize("python"))
    print(lemmatizer.lemmatize("better"))
    print(lemmatizer.lemmatize("better", pos="a"))
    print(lemmatizer.lemmatize("worst", pos="a"))
    print(lemmatizer.lemmatize("running"))
    print(lemmatizer.lemmatize("running", pos="v"))
    print(lemmatizer.lemmatize("quickly", pos="s"))


if __name__ == "__main__":
    # main execution
    main()
