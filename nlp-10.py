# WORDNET
# !/anaconda/bin/python python 3

from nltk.corpus import wordnet


def main():
    # main code here
    synonyms = []
    antonyms = []

    syns = wordnet.synsets("program")

    # synset
    print(syns[0].name())
    print("\n")
    # just the word
    print(syns[0].lemmas()[0].name)
    # definition
    print(syns[0].definition)
    # examples
    print(syns[0].examples)

    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    print(set(synonyms))
    print(set(antonyms))

    w1 = wordnet.synset("ship.n.01")
    w2 = wordnet.synset("boat.n.01")

    print(w1.wup_similarity(w2))

    w1 = wordnet.synset("ship.n.01")
    w2 = wordnet.synset("car.n.01")

    print(w1.wup_similarity(w2))

    w1 = wordnet.synset("ship.n.01")
    w2 = wordnet.synset("cat.n.01")

    print(w1.wup_similarity(w2))


if __name__ == "__main__":
    # main execution
    main()
