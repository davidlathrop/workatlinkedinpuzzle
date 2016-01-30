import json
import os
import re
import string
import time

cols_tests= [
      '.(LN|K|D)*',
      '([MBERS]*)\\1',
      '(ENG|INE|E|R)*',
      '[LINKED]*IN'
]

row_match = []
col_regex = []
col_match = [[],[],[],[]]



def compile_reg():
    global col_regex, cols_tests
    _test = '^{0}$'

    col_regex = [re.compile(_test.format(col)) for col in cols_tests]


def find_matches():
    global col_match

    for one in string.ascii_uppercase:
        for two in string.ascii_uppercase:
            for three in string.ascii_uppercase:
                for four in string.ascii_uppercase:
                    col = '{}{}{}{}'.format(one,two,three,four)
                    
                    for idx, col_test in enumerate(col_regex):
                        if col_test.match(col):
                            col_match[idx].append(col)

def write_matches():
    global col_match
    pth = os.path.dirname(os.path.abspath(__file__))
    fp = '{}/cols.txt'.format(pth)

    fd = open(fp, 'w+')

    for col in col_match:
        json.dump(col, fd)
        fd.write("\n")

    fd.close()


def col_main():
    compile_reg()
    find_matches()
    write_matches()


if __name__ == "__main__":
    col_main()