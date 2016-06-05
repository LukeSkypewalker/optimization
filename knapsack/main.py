import os
import greed_sorted_by_value as greed_value
import greed_sorted_by_density as greed_density
# import branch_n_bound as branch_unsorted
import branch_n_bound_sorted_weight as branch_sorted
import branch_n_bound_sorted_weight_relax as branch_relax
from common import *


files = os.listdir('data')
print files
for f in (files[14], files[6], files[10], files[12]):
    print f
    # branch_un = branch_unsorted.solve_it(get_data('./data/'+f))
    # print branch_un
    branch_s = branch_sorted.solve_it(get_data('./data/' + f))
    print branch_s
    branch_d = branch_relax.solve_it(get_data('./data/' + f))
    print branch_d


# for f in files:
#     val = greed_value.solve_it(get_data('./data/'+f)).split()[0]
#     dense = greed_density.solve_it(get_data('./data/'+f)).split()[0]
#     diff = int(val)-int(dense)
#     print f, val, dense, diff
