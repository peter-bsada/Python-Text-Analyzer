"""
analyzer, alla def functioner.
"""


from collections import Counter
import re


def lines(filename):
    """
    Hur många lines det finns
    """
    emptyLines = 0

    with open(filename) as filehandle:
        for line in filehandle:
            if line.strip():
                emptyLines += 1
    print("lines:" + str(emptyLines))


def words(filename):
    """
    Hur många ord det finns
    """
    emptyWords = 0
    with open(filename, "r") as f:
        for word in f:
            wordsSplit = word.split()
            emptyWords += len(wordsSplit)

    print("words: " + str(emptyWords))

def letter(content):
    """
    Hur många lettes det finns
    """
    letter_sum = 0
    for letter1 in content.lower():
        if letter1.isalpha():
            letter_sum = letter_sum + 1
    print("letters: " + str(letter_sum))





def word_frequency(filename):
    """
    Analyzes word frequency
    """
    with open(filename) as filehandle:
        content = filehandle.read().lower()
        all_words = re.findall(r'\w+', content)
        most_common_words = Counter(all_words).most_common(7)
        for key, value in most_common_words:
            result_word = (value / len(all_words)) * 100
            print(key + ": " + str(value) + " | " + str(round(result_word, 1)) + "%")


def letter_frequency(filename):
    """
    Analyzes letter frequency
    """
    with open(filename) as fh:
        content = fh.read().lower()
        letter_list = []
        for word in content:
            for letter2 in word:
                split_letters = letter2.split()
                letter_list += split_letters
                if split_letters == ",":
                    letter_list.remove(",")
                elif split_letters == ".":
                    letter_list.remove(".")
                elif split_letters == "-":
                    letter_list.remove("-")

        most_common_letter = Counter(letter_list).most_common(7)
        for key_one, value_one in most_common_letter:
            result_letter = (value_one / len(letter_list)) * 100
            print(key_one + ": " + str(value_one) + " | " + str(round(result_letter, 1)) + "%")
