from key_layout.data.data import *
from key_layout.flow_processor import *
from itertools import permutations
from itertools import combinations


def get_best_hand_perm_bruteforce(letters):
    hand_perms = list(permutations(letters))
    best_hand = hand_perms[0]
    best_score = 0
    for hand in hand_perms:
        res = calc_hand_flow(hand, bigrams)
        if res > best_score:
            best_score = res
            best_hand = hand
    print(best_score, *best_hand)
    return round(best_score)


def get_best_hand_perm_smart(letters):
    best_hand = letters
    best_score = 0
    for comb in list(combinations(letters[0:5], 4)):
        for perm0 in list(permutations(comb)):
            not_in_comb = list([x for x in letters if x not in comb])
            for perm1 in list(permutations(not_in_comb)):
                hand = perm0 + perm1
                res = calc_hand_flow(hand, bigrams)
                if res > best_score:
                    best_score = res
                    best_hand = hand

    print(best_score, *best_hand)

    return round(best_score)


if __name__ == '__main__':
    from itertools import combinations

    import doctest
    doctest.testmod()

    # left_hand_layout_combs = combinations(letters8, len(letters8) // 2)
    # comb_sum = calc_combs_sums(left_hand_layout_combs, bigrams8)
    # comb_sum.sort(key=lambda comb: comb[1])
    # print(*comb_sum, sep='\n')
    # res = calc(['R', 'O', 'I', 'A', 'N', 'S', 'E', 'T'], bigrams8)
    aest_niro = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B',
                 'O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']
    aser_nito = ['A', 'S', 'E', 'R', 'D', 'U', 'C', 'F', 'G', 'B',
                 'O', 'T', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']
    asdf_jkl_ = ['A', 'S', 'D', 'F', 'W', 'E', 'C', 'V', 'R', 'G',
                 'Y', 'L', 'K', 'J', 'O', 'I', 'N', 'M', 'U', 'H']
    aset_nior = ['A', 'S', 'E', 'T', 'D', 'F', 'C', 'V', 'P', 'G',
                 'R', 'O', 'I', 'N', 'L', 'H', 'Y', 'M', 'U', 'W']
    work_man_ = ['A', 'S', 'H', 'T', 'D', 'R', 'M', 'C', 'W', 'G',
                 'I', 'O', 'E', 'N', 'P', 'U', 'L', 'K', 'F', 'Y']
    _ = ['A', 'S', 'H', 'T', 'D', 'R', 'M', 'C', 'W', 'G',
         'I', 'O', 'E', 'N', 'P', 'U', 'L', 'K', 'F', 'Y']
    freq1 = ['S', 'N', 'R', 'H', 'D', 'L', 'C', 'M', 'F', 'W']
    freq2 = ['E', 'A', 'O', 'I', 'T', 'P', 'Y', 'G', 'U', 'B']

    aest_niro1 = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    aest_niro2 = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    # res = calc_layout(aest_niro, bigrams)
    # res = calc_layout(aser_nito, bigrams)
    # res = calc_layout(aset_nior, bigrams)
    # res = calc_layout(asdf_jkl_, bigrams)
    # res = calc_layout(work_man_, bigrams)

    res = get_best_hand_perm_smart(freq1)
    # res = get_best_hand_perm_smart(freq2)
    print(res)
    # print(total_probability)
    # print(res / total_probability)
