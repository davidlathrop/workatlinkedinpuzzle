from common import RegCommon

cols_tests = [
    '.(LN|K|D)*',
    '([MBERS]*)\\1',
    '(ENG|INE|E|R)*',
    '[LINKED]*IN'
]

col_regex = []


def find_matching_cols():
    for word in RegCommon.permutations():
        for idx, col_test in enumerate(col_regex):
            if col_test.match(word):
                try:
                    RegCommon.col_matches[idx].append(word)
                except IndexError:
                    RegCommon.col_matches.append([])


def col_main():
    global col_regex
    col_regex = RegCommon.compile_regex(cols_tests)
    find_matching_cols()


if __name__ == "__main__":
    col_main()
