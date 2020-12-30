"""
Project 1.1: Pig Latin translator.

Objective: Write a pig latin translator following established style guidelines.

Pseudocode:
    Take user input
    Replace words with pig latin
        (Use slicing and indexing)
    Return translated sentence
"""
import sys


def main():
    """Translates a user's input into pig latin."""
    word = input("What word would you like to translate?")
    pig_latin_sentence = []

    VOWELS = "aeiouy"

    while True:
        if word[0] in VOWELS:
            pig_latin = word + "way"
        else:
            pig_latin = word[1:] + word[0] + "ay"

        print(f"{pig_latin}", file=sys.stderr)

        try_again = input("Try again? (Press Enter, else q to quit.)\n")
        if try_again.lower() == "q":
            sys.exit()


if __name__ == "__main__":
    main()
