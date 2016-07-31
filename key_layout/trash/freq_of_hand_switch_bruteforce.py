from datetime import datetime
from itertools import combinations

from key_layout.data.data import letters26, bigrams
from key_layout.data.data_helper import store_to_file
from key_layout.trash.freq_of_hand_switch_processor import calc_combs_sums

# left_hand_layout_combs = combinations(letters, len(letters) // 2)
left_hand_layout_combs = combinations(letters26, 15)


time_start = datetime.now()
comb_sum = calc_combs_sums(left_hand_layout_combs, bigrams)
comb_sum.sort(key=lambda comb: comb[1])
time_end = datetime.now()
print('time', time_end - time_start)


print(*comb_sum, sep='\n')
total_probability = sum(i for _, _, i in bigrams)
print('hand switching frequency:', comb_sum[-1][1] / total_probability)


store_to_file(comb_sum, 'result.txt')
