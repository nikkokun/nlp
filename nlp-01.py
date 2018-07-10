# TOKENIZING
# !/anaconda/bin/python python 3

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

# tokenizing - word tokenizers separates by words... sentence tokenizers separates by sentences
# lexicons and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their meanings

# nltk.download()

example_text = "Hello Mr. T. Hagino, how are you doing today? The weather is great and Python is awesome. The sky is pinkish blue, you should not eat cardboard."


def main():
    print(sent_tokenize(example_text))
    print(word_tokenize(example_text))

    for x in word_tokenize(example_text):
        print(x)

    print("\n")
    for x in sent_tokenize(example_text):
        print(x + " " + str(len(x)) + "\n")


if __name__ == "__main__":
    main()
