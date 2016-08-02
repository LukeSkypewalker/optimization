from datetime import datetime
from itertools import permutations
from key_layout.data.data import freq
from key_layout.hand_score_calc import calc_hand_score


def get_best_hand_perm(letters):
    letters.sort(key=lambda letter: freq[letter], reverse=True)
    hand_permutations = get_smart_permutations(letters)

    best_hand = letters
    best_score = 0
    for hand in hand_permutations:
        scores = calc_hand_score(hand)
        if scores > best_score:
            best_score = scores
            best_hand = hand

    return best_score, best_hand


def get_smart_permutations(letters):
    perms = []
    for comb in list(combinations(letters[0:5], 4)):
        not_in_comb = list([x for x in letters if x not in comb])
        for perm4 in list(permutations(comb)):
            for perm6 in list(permutations(not_in_comb)):
                perm = perm4 + perm6
                perms.append(perm)
    return perms


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
    res = get_best_hand_perm(aest)
    print(res)
    time_end = datetime.now()
    print('time', time_end - time_start)

    # res = get_best_hand_perm(niro)
    # print(res)
    # time_end = datetime.now()
    # print('time', time_end - time_start)
