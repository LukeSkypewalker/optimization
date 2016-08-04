from datetime import datetime
from key_layout.data.data import letters20, bigrams20
from key_layout.hand_permutations import process_hand_perm


# TODO:


def process_comb(left_hand):
    # """
    # >>> (['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'], bigrams_aest)
    # 673711667.1999998
    # """

    right_hand = [letter for letter in letters20 if letter not in left_hand]
    best_right = process_hand_perm(right_hand, bigrams20)
    best_left = process_hand_perm(left_hand, bigrams20)
    print(best_left)
    print(best_right)
    return best_left[0] + best_left[1] + best_right[1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']

    time_start = datetime.now()
    res = process_comb(aest)
    print(res)
    time_end = datetime.now()
    print('time', time_end - time_start)