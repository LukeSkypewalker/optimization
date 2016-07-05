def calc_combs_sums(left_hand_combs, bigrams):
    return [(comb, calc_sum_freq(bigrams, comb)) for comb in left_hand_combs]


def calc_sum_freq(bigrams, left_hand_comb):
    return sum(b[2] for b in bigrams if (b[0] in left_hand_comb) != (b[1] in left_hand_comb))


if __name__ == '__main__':
    from itertools import combinations
    from key_layout.data import *

    left_hand_layout_combs = combinations(letters8, len(letters8) // 2)
    comb_sum = calc_combs_sums(left_hand_layout_combs, bigrams)
    comb_sum.sort(key=lambda comb: comb[1])
    print(*comb_sum, sep='\n')

