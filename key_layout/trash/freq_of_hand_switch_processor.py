from key_layout.data.data import *


def calc_combs_sums(left_hand_combs, bigrams):
    return [(comb, calc_comb_sum(comb, bigrams)) for comb in left_hand_combs]


def calc_comb_sum(left_hand_comb, bigrams):
    return sum(b[2] for b in bigrams if (b[0] in left_hand_comb) != (b[1] in left_hand_comb))


def calc_combs_sums_homerow(left_hand_combs, bigrams):
    return [(comb, calc_comb_sum_homerow(comb, bigrams)) for comb in left_hand_combs]


def calc_comb_sum_homerow(left_hand_comb, bigrams):
    return sum(b[2] for b in bigrams
               if ((b[0] in left_hand_comb) != (b[1] in left_hand_comb)) or
               (b[0] in letters8 and b[1] in letters8))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    res = calc_comb_sum(aest, bigrams)
    print(res)
    res = calc_comb_sum(niro, bigrams)
    print(res)
