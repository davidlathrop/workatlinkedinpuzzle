from common import RegCommon

rows_tests = [
    'R+D',
    '[^WORK]*ING?',
    '.*[IN].*',
    'C{0}N[NECT]*'
]

row_regex = []


def find_matching_rows():    
    for word in RegCommon.permutations():
        for idx, row_test in enumerate(row_regex):
            if row_test.match(word):
                try:
                    RegCommon.row_matches[idx].append(word)
                except IndexError:
                    RegCommon.row_matches.append([])


def row_main():
    global row_regex
    row_regex = RegCommon.compile_regex(rows_tests)
    find_matching_rows()


if __name__ == "__main__":
    row_main()
