"""
Min main file
"""
import menu
import analyzer

filename = "phil.txt"
with open(filename) as filehandle:
    content = filehandle.read()

while True:
    choice = input("-->")
    if choice == "menu":
        menu.menu()

    if choice == "lines":
        analyzer.lines(filename)

    if choice == "words":
        analyzer.words(filename)

    if choice == "letters":
        analyzer.letter(content)

    if choice == "word_frequency":
        analyzer.word_frequency(filename)

    if choice == "letter_frequency":
        analyzer.letter_frequency(filename)

    if choice == "all":
        analyzer.lines(filename)
        analyzer.words(filename)
        analyzer.letter(content)
        analyzer.word_frequency(filename)
        analyzer.letter_frequency(filename)

    if choice == "change":
        fil = input("file: ")

    if choice == "q" or choice == "quit":
        break
