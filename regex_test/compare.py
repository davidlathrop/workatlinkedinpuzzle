import json
import os


row_matches = []
col_matches = []
grids = []


def load_rows():
    global row_matches
    pth = os.path.dirname(os.path.abspath(__file__))
    fp = '{}/rows.txt'.format(pth)
    with open(fp, 'r') as fd:
        for line in fd:
            row_matches.append(frozenset(json.loads(line)))


def load_cols():
    global col_matches
    pth = os.path.dirname(os.path.abspath(__file__))
    fp = '{}/cols.txt'.format(pth)
    with open(fp, 'r') as fd:
        for line in fd:
            col_matches.append(json.loads(line))


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
        print("Before: ", len(items))
        for item in items:
            if item[0] not in possible_letters:
                continue

            new_group[idx].append(item)
        print("After: ", len(new_group[idx]))

    return new_group


def narrow_choices():
    global col_matches, row_matches

    col_letters = narrow_letters(col_matches)
    row_matches = reduce_matches(col_letters, row_matches)

    row_letters = narrow_letters(row_matches)
    col_matches = reduce_matches(row_letters, col_matches)
    

def compare_cols_to_rows():
    global col_matches, grids, row_matches
    
    one, two, three, four = col_matches
      
    for r1 in one:
        for r2 in two:
            for r3 in three:
                for r4 in four:
                    rows = [[r1[idx],r2[idx],r3[idx],r4[idx]] for idx in range(0,4)]
                    grid = [''.join(row) in row_matches[idx] for idx, row in enumerate(rows)]
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
    load_rows()
    load_cols()
    narrow_choices()
    compare_cols_to_rows()
    write_grids()


if __name__ == "__main__":
    compare_main()