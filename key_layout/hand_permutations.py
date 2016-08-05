import timeit
from datetime import datetime
from itertools import permutations, combinations
from pprint import pprint

from key_layout.data.data import freq, bigrams20, store_to_file
from key_layout.hand_score_calc import calc_hand_score


def process_hand_perm(letters, bigrams, perm_function):

    bigrams_filtered = filter_bigrams(letters, bigrams)

    letters.sort(key=lambda letter: freq[letter], reverse=True)

    hand_permutations = perm_function(letters)

    best_hand = letters
    best_flow_score = 0
    data = []
    for hand in hand_permutations:
        score = calc_hand_score(hand, bigrams_filtered)
        data.append([hand, score])
        if score > best_flow_score:
            best_flow_score = score
            best_hand = hand

    # data.sort(key=lambda x: x[1], reverse=True)
    # store_to_file(data, 'bbb.txt')

    return best_hand, best_flow_score


def get_smart_permutations_right(letters):
    perms = []
    for comb in list(combinations(letters[0:5], 4)):
        not_in_comb = list([x for x in letters if x not in comb])
        for perm4 in list(permutations(comb)):
            for perm6 in list(permutations(not_in_comb)):
                perm = perm4 + perm6
                perms.append(perm)
    return perms


def get_smart_permutations_left(letters):
    perms = []
    for perm4 in list(permutations(letters[0:4])):
        for perm6 in list(permutations(letters[4:])):
            perm = perm4 + perm6
            perms.append(perm)
    return perms


def filter_bigrams(hand, bigrams):
    return [b for b in bigrams if b[0] in hand and b[1] in hand]


# def process_bigrams(hand, bigrams):
#     bigrams_filtered = []
#     hand_switch_score = 0
#     for b in bigrams:
#
#         is_b0_in_hand = b[0] in hand
#         is_b1_in_hand = b[1] in hand
#
#         if not is_b0_in_hand and not is_b1_in_hand:
#             continue
#
#         if is_b0_in_hand and is_b1_in_hand:
#             bigrams_filtered.append(b)
#         else:
#             hand_switch_score += b[2]
#
#     return hand_switch_score, bigrams_filtered


if __name__ == '__main__':
    from itertools import combinations
    import doctest

    doctest.testmod()

    freq1 = ['S', 'N', 'R', 'H', 'D', 'L', 'C', 'M', 'F', 'W']
    freq2 = ['E', 'A', 'O', 'I', 'T', 'P', 'Y', 'G', 'U', 'B']

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    worst = ['E', 'A', 'S', 'R', 'L', 'D', 'M', 'P', 'Y', 'B']
    # time_start = datetime.now()
    # res = process_hand_perm(aest, bigrams20)
    # print(res)
    # time_end = datetime.now()
    # print('time ', time_end - time_start)

    # left = get_smart_permutations_left(worst)
    left = process_hand_perm(worst, bigrams20)
    pprint(left)

    # print('timeit ', timeit.timeit(
    #     'process_hand_perm(aest, bigrams)',
    #     setup="from __main__ import process_hand_perm, aest, bigrams",
    #     number=1))

    # res = get_best_hand_perm(niro)
    # print(res)
    # time_end = datetime.now()
    # print('time', time_end - time_start)
