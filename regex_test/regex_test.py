import time

from compare import compare_main
from gen_cols import col_main
from gen_rows import row_main


s = time.time()
row_main()
col_main()
compare_main()
e = time.time()

print("Runtime: {}".format(e-s))
