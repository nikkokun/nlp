# NAMED ENTITY
# !/anaconda/bin/python python 3

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEntity = nltk.ne_chunk(tagged)
            namedEntity.draw()

    except Exception as e:
        print(str(e))


def main():
    # main code here
    process_content()


if __name__ == "__main__":
    # main execution
    main()
