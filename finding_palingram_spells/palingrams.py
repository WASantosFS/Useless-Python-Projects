"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load("2of4brif.txt")


def palindrome():
    """Determine if a word is palindromic or not.

    :return: A list of palindromic words in the given file.
    """
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)
    print(f"Number of palindromes found = {len(pali_list)}")
    print(*pali_list, sep="\n")


def find_palingrams():
    """Find dictionary palingrams, using lists. Takes about 2 minutes to run.

    :return: A list of palingrams based off of the given file.
    """
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list


def palingrams_opt():
    """Find dictionary palingrams, using sets.

    :return: A list of palingrams based off of the given file.
    """
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    pali_list.append((word, rev_word[end - i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in words:
                    pali_list.append((rev_word[:end - i], word))
    return pali_list


def main():
    palingrams = palingrams_opt()
    palingrams_sorted = sorted(palingrams)

    print(f"Number of palingrams = {len(palingrams_sorted)}")
    for first, second in palingrams_sorted:
        print(f"{first} {second}")


if __name__ == "__main__":
    main()
