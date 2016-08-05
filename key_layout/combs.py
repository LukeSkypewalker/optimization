# TODO:
from datetime import datetime
from itertools import combinations
from pprint import pprint

from tornado import concurrent

from key_layout.comb_processor import process_comb
from key_layout.data.data import letters20, freq, bigrams20, letters18, bigrams18
from key_layout.trash.freq_of_hand_switch_processor import calc_combs_sums


def get_combs(letters_set):
    letters = sorted(letters_set, key=lambda letter: freq[letter], reverse=True)
    combs = []
    letters_top9 = letters[0:9]
    letters_last = letters[9:]
    for comb4 in list(combinations(letters_top9, 4)):
        for comb6 in list(combinations(letters_last, 5)):
            comb = list(comb4 + comb6)
            combs.append(comb)
    return combs


if __name__ == '__main__':
    combs = get_combs(letters18)

    time_start = datetime.now()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = [executor.submit(process_comb, hand, bigrams18, letters18) for hand in combs[:16]]
    time_end = datetime.now()
    print('time', time_end - time_start)

    # with open('ccc.txt', 'w') as file:
    #     file.write('\n'.join('%s %s %s %s %s %s %s %s %s %s' % x for x in combs))

    # combs_hand_switch = calc_combs_sums(combs, bigrams20)
    # combs_hand_switch.sort(key=lambda x: x[1], reverse=True)
    # with open('xxx.txt', 'w') as file:
    #     file.write('\n'.join('%s %s' % x for x in combs_hand_switch))

