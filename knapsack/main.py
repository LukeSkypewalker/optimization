import os
import greed_sorted_by_value as greed_value
import greed_sorted_by_density as greed_density
import branch_n_bound as branch
import branch_n_bound_sorted_weight as branch_sorted
from common import *





# files = os.listdir('data')
# for f in files:
#     val = greed_value.solve_it(get_data('./data/'+f)).split()[0]
#     dense = greed_density.solve_it(get_data('./data/'+f)).split()[0]
#     diff = int(val)-int(dense)
#     print f, val, dense, diff
