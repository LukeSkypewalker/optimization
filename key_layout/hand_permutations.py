import timeit
from datetime import datetime
from itertools import permutations, combinations

from key_layout.data.data import freq, bigrams20
from key_layout.hand_score_calc import calc_hand_score


def process_hand_perm(letters, bigrams):

    hand_switch_score, bigrams_filtered = process_bigrams(letters, bigrams)

    letters.sort(key=lambda letter: freq[letter], reverse=True)
    hand_permutations = get_smart_permutations(letters)

    best_hand = letters
    best_flow_score = 0
    for hand in hand_permutations:
        scores = calc_hand_score(hand, bigrams_filtered)
        if scores > best_flow_score:
            best_flow_score = scores
            best_hand = hand

    return hand_switch_score, best_flow_score, best_hand


def get_smart_permutations(letters):
    perms = []
    for comb in list(combinations(letters[0:5], 4)):
        not_in_comb = list([x for x in letters if x not in comb])
        for perm4 in list(permutations(comb)):
            for perm6 in list(permutations(not_in_comb)):
                perm = perm4 + perm6
                perms.append(perm)
    return perms


def process_bigrams(hand, bigrams):
    bigrams_filtered = []
    hand_switch_score = 0
    for b in bigrams:

        is_b0_in_hand = b[0] in hand
        is_b1_in_hand = b[1] in hand

        if not is_b0_in_hand and not is_b1_in_hand:
            continue

        if is_b0_in_hand and is_b1_in_hand:
            bigrams_filtered.append(b)
        else:
            hand_switch_score += b[2]

    return hand_switch_score, bigrams_filtered


if __name__ == '__main__':
    from itertools import combinations
    import doctest

    doctest.testmod()

    freq1 = ['S', 'N', 'R', 'H', 'D', 'L', 'C', 'M', 'F', 'W']
    freq2 = ['E', 'A', 'O', 'I', 'T', 'P', 'Y', 'G', 'U', 'B']

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    time_start = datetime.now()
    res = process_hand_perm(aest, bigrams20)
    print(res)
    time_end = datetime.now()
    print('time', time_end - time_start)

    print(timeit.timeit(
        'process_hand_perm(aest, bigrams)',
        setup="from __main__ import process_hand_perm, aest, bigrams",
        number=1))

    # res = get_best_hand_perm(niro)
    # print(res)
    # time_end = datetime.now()
    # print('time', time_end - time_start)
