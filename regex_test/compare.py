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


def compare_cols_to_rows():
    global col_matches, grids, row_matches
    
    one, two, three, four = col_matches
    one = [r for r in one if r[0] == 'R']  # I happen to know that this column starts with R
    
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
            json.dump(grid, fd)
            fd.write('\n')

def compare_main():
    load_rows()
    load_cols()
    compare_cols_to_rows()
    write_grids()


if __name__ == "__main__":
    compare_main()