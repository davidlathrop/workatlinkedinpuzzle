import json
import os

from common import RegCommon

grids = []


def narrow_letters(groups):
    group_letters = []
    for item in groups[0]:
        while len(group_letters) < len(item):
            group_letters.append(set())

        for lidx, letter in enumerate(item):
            group_letters[lidx].add(letter)

    return group_letters


def reduce_matches(letters, group):
    new_group = []
    for idx, items in enumerate(group):
        possible_letters = letters[idx]
        new_group.append([])
        for item in items:
            if item[0] not in possible_letters:
                continue

            new_group[idx].append(item)

    return new_group


def narrow_choices():
    col_letters = narrow_letters(RegCommon.col_matches)
    RegCommon.row_matches = reduce_matches(col_letters, RegCommon.row_matches)

    row_letters = narrow_letters(RegCommon.row_matches)
    RegCommon.col_matches = reduce_matches(row_letters, RegCommon.col_matches)
    

def compare_cols_to_rows():
    global grids
    
    one, two, three, four = RegCommon.col_matches
      
    for r1 in one:
        for r2 in two:
            for r3 in three:
                for r4 in four:
                    rows = [[r1[idx],r2[idx],r3[idx],r4[idx]] for idx in range(0,4)]
                    grid = [''.join(row) in RegCommon.row_matches[idx] for idx, row in enumerate(rows)]
                    if all(grid): 
                        grids.append(rows)


def write_grids():
    global grids
    pth = os.path.dirname(os.path.abspath(__file__))
    fp = '{}/matching_grids.txt'.format(pth)
    with open(fp, 'w+') as fd:
        for grid in grids:
            lines = [' '.join(line) + '\n' for line in grid]
            fd.writelines(lines)


def compare_main():
    narrow_choices()
    compare_cols_to_rows()
    write_grids()


if __name__ == "__main__":
    compare_main()