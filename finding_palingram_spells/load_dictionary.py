"""Load a text file as a list."""
import sys


def load(file):
    """Open a text file and return a list of lowercase strings.

    :param file: Text file name (and directory path, if needed).
    :exception IOError: If filename not found.
    :return: A list of all words in a text file in lower case.
    """
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as error:
        print(f"{error}\nError opening {file}", file=sys.stderr)
        sys.exit(1)
