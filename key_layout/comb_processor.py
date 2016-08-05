from datetime import datetime

from key_layout.balance_processor import calc_disbalance_hands
from key_layout.hand_permutations import process_hand_perm, get_smart_permutations_right, get_smart_permutations_left

# TODO:
from key_layout.trash.freq_of_hand_switch_processor import calc_comb_sum


def process_comb(left_hand, bigrams, letters):

    comb_hand_switch = calc_comb_sum(left_hand, bigrams)
    disbalance_hands = calc_disbalance_hands(left_hand)
    right_hand = [letter for letter in letters if letter not in left_hand]
    best_left = process_hand_perm(left_hand, bigrams, get_smart_permutations_left)
    best_right = process_hand_perm(right_hand, bigrams, get_smart_permutations_right)
    score = round((comb_hand_switch + best_left[1] + best_right[1])/disbalance_hands)
    print(best_left[0], best_right[0], score)
    return score


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']

    time_start = datetime.now()
    res = process_comb(aest)
    print(res)
    time_end = datetime.now()
    print('time', time_end - time_start)