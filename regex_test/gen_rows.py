import json
import os
import re
import string
import time

rows_tests = [
      'R+D',
      '[^WORK]*ING?',
      '.*[IN].*',
      'C{0}N[NECT]*'
]

grids = []
row_permutations = []
row_matches = []
row_regex = []


def compute_all_permutations():
    global row_permutations
    for one in string.ascii_uppercase:
        for two in string.ascii_uppercase:
            for three in string.ascii_uppercase:
                for four in string.ascii_uppercase:
                    word = "{}{}{}{}".format(one, two, three, four)
                    row_permutations.append(word)


def compile_tests():
    global row_regex, col_regex, rows_tests

    _test = '^{0}$'
    for row in rows_tests:
        row_regex.append(re.compile(_test.format(row)))


def find_matching_rows():
    global row_matches
    for word in row_permutations:
        for idx, row_test in enumerate(row_regex):
            if row_test.match(word):
                try:
                    row_matches[idx].append(word)
                except IndexError:
                    row_matches.append([word, ])


def write_matching_rows():
    global row_matches
    pth = os.path.dirname(os.path.abspath(__file__))
    fp = '{}/rows.txt'.format(pth)

    fd = open(fp, 'w+')

    for row in row_matches:
        json.dump(row, fd)
        fd.write("\n")

    fd.close()

def row_main():
    compute_all_permutations()
    compile_tests()
    find_matching_rows()
    write_matching_rows()


if __name__ == "__main__":
    row_main()


