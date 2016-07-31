from itertools import permutations

from key_layout.layout_permutations import calc_layout_flow

# left_hand_layout_combs = combinations(letters8, len(letters8) // 2)
# comb_sums = calc_combs_sums(left_hand_layout_combs, bigrams8)

layouts = list(permutations(letters8))
# print(*left_hand_layout_combs, sep='\n')
scores = [(layout, calc_layout_flow(layout, bigrams8)) for layout in layouts]

scores.sort(key=lambda comb: comb[1])
data = [(x, x[1]/total_probability8) for x in scores]
print(*data, sep='\n')


