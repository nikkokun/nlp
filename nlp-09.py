# CORPORAS
# !/anaconda/bin/python python 3

from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer


def main():
    # main code here
    sample = gutenberg.raw("bible-kjv.txt")
    tok = sent_tokenize(sample)
    for x in range(15):
        print(str(x) + " " + tok[x] + "\n")


if __name__ == "__main__":
    # main execution
    main()
