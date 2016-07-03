from key_layout.bigpams_processor import *
from key_layout.data import *

aset_nior = ('Q', 'D', 'F', 'P', 'K',
             'A', 'S', 'E', 'T', 'G',
             'Z', 'X', 'C', 'V', 'B')

aest = ('Q', 'U', 'D', 'G', 'K',
             'A', 'E', 'S', 'T',
             'Z', 'X', 'C', 'F')

qwerty = ('Q', 'W', 'E', 'R', 'T',
          'A', 'S', 'D', 'F', 'G',
          'Z', 'X', 'C', 'V', 'B')

workman = ('Q', 'D', 'R', 'W', 'B',
           'A', 'S', 'H', 'T', 'G',
           'Z', 'X', 'M', 'C', 'V')

norman = ('Q', 'W', 'D', 'F', 'K',
          'A', 'S', 'E', 'T', 'G',
          'Z', 'X', 'C', 'V', 'B')


combs = (aset_nior, qwerty, aest, norman,workman)

comb_sum = calc_combs_sums(combs, bigrams)
comb_sum.sort(key=lambda comb: comb[1])

for comb in comb_sum:
    print(comb)
    print('hand switching frequency:', comb[1] / total_probability, '\n')

store_to_file(comb_sum, 'full.txt')
