import concurrent.futures
from datetime import datetime
from itertools import permutations
from pprint import pprint

from key_layout.data.data import freq, bigrams
from key_layout.hand_score_calc import calc_hand_score


def get_smart_permutations(letters):
    perms = []
    for comb in list(combinations(letters[0:5], 4)):
        not_in_comb = list([x for x in letters if x not in comb])
        for perm4 in list(permutations(comb)):
            for perm6 in list(permutations(not_in_comb)):
                perm = perm4 + perm6
                perms.append(perm)
    return perms


def process_bigrams(letters, bigrams):
    # bi = [b for b in bigr ]
    bigrams_filtered = []
    hand_switch_score = 0
    for b in bigrams:
        if b[0] == b[1]:
            continue

        is_b0_in_hand = b[0] in letters
        is_b1_in_hand = b[1] in letters

        if not is_b0_in_hand and not is_b1_in_hand:
            continue

        if is_b0_in_hand and is_b1_in_hand:
            bigrams_filtered.append(b)
        else:
            hand_switch_score += b[2]

    return hand_switch_score, bigrams_filtered


def get_best_hand_perm(letters, bigrams):

    hand_switch_score, bigrams_filtered = process_bigrams(letters, bigrams)

    letters.sort(key=lambda letter: freq[letter], reverse=True)
    hand_permutations = get_smart_permutations(letters)

    best_hand = letters
    best_score = 0
    for hand in hand_permutations:
        scores = calc_hand_score(hand, bigrams_filtered)
        if scores > best_score:
            best_score = scores
            best_hand = hand

    return best_score, best_hand


# def filter_bigrams(letters, bigrams_filtered):
#     return [b for b in bigrams_filtered if (b[0] in letters and b[1] in letters and b[0] != b[1])]


# def get_best_hand_perm_multiprocess(letters):
#     letters.sort(key=lambda letter: freq[letter], reverse=True)
#     hand_permutations = get_smart_permutations(letters)
#     bigrams_filtered = filter_bigrams(letters, bigrams)
#
#     best_hand = letters
#     best_score = 0
#
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future = [executor.submit(calc_hand_score, hand, bigrams_filtered) for hand in hand_permutations]
#         # for hand, score in zip(hand_permutations, future.result()):
#         #     if score > best_score:
#         #         best_score = score
#         #         best_hand = hand
#
#     return best_score, best_hand


# def get_best_hand_perm_multiprocess(letters):
#     letters.sort(key=lambda letter: freq[letter], reverse=True)
#     hand_permutations = get_smart_permutations(letters)
#     bigrams_filtered = filter_bigrams(letters, bigrams)
#
#     best_hand = letters
#     best_score = 0
#
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for hand, score in zip(hand_permutations, executor.map(calc_hand_score, hand_permutations, bigrams_filtered)):
#             if score > best_score:
#                 best_score = score
#                 best_hand = hand
#
#     return best_score, best_hand


# def get_best_hand_perm_bruteforce(letters):
#     hand_perms = list(permutations(letters))
#     best_hand = hand_perms[0]
#     best_score = 0
#     for hand in hand_perms:
#         res = calc_flow(hand)
#         if res > best_score:
#             best_score = res
#             best_hand = hand
#     print(best_score, *best_hand)
#     return round(best_score)


if __name__ == '__main__':
    from itertools import combinations

    import doctest

    doctest.testmod()

    freq1 = ['S', 'N', 'R', 'H', 'D', 'L', 'C', 'M', 'F', 'W']
    freq2 = ['E', 'A', 'O', 'I', 'T', 'P', 'Y', 'G', 'U', 'B']

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    time_start = datetime.now()
    # res = get_best_hand_perm_multiprocess(aest)
    res = get_best_hand_perm(aest, bigrams)
    print(res)
    time_end = datetime.now()
    print('time', time_end - time_start)

    # res = get_best_hand_perm(niro)
    # print(res)
    # time_end = datetime.now()
    # print('time', time_end - time_start)
