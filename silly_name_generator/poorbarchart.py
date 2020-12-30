"""
Project 1.2: Poor Man's Barchart.

Objective: Write a pig latin translator following established style guidelines.

Pseudocode:
    Take user input
    Break user input into letters/characters
    Count letters
    Print result as letter * count.
"""
import string
from pprint import pprint as pp


def main():
    """Create a barchart expression of a sentence."""
    user_input = input("Sentence you'd like to chartify: ").lower()
    unique_letters = sorted(set(user_input))
    letter_dictionary = {}

    while True:

        for character in unique_letters:
            if character not in string.ascii_lowercase:  # Filters out all non-letters.
                continue
            letter_dictionary[character] = list(character * user_input.count(character))

        pp(letter_dictionary)

        try_again = input("Try again? (Press Enter, else q to quit.)\n")
        if try_again.lower() == "q":
            break


if __name__ == "__main__":
    main()
