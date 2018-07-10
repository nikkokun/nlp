# STEMMING
# !/anaconda/bin/python python 3
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# Both have the meanings but different words
# I was taking a ride in the car.
# I was riding in the car.

def main():
    # main code here
    ps = PorterStemmer()
    example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
    for word in example_words:
        print(ps.stem(word))

    new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
    words = word_tokenize(new_text)
    print('\n')
    for word in words:
        print(ps.stem(word))


if __name__ == "__main__":
    # main execution
    main()
