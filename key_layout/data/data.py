from collections import namedtuple

Bigram = namedtuple("Bigram", ['a', 'b', 'frequency'])

from key_layout.data.data_helper import *

# bigrams = get_bigrams_list(get_data('data/bigrams26.txt'))
# bigrams22 = get_bigrams_list(get_data('data/bigrams22.txt'))
bigrams18 = get_bigrams_list(get_data('data/bigrams18.txt'))
bigrams20 = get_bigrams_list(get_data('data/bigrams20.txt'))
bigrams_aest = get_bigrams_list(get_data('data/bigrams_aest.txt'))
# bigrams8 = get_bigrams_list(get_data('data/bigrams8.txt'))

# letters26 = ('E', 'T', 'A', 'O', 'I', 'N', 'S', 'R',
#              'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P',
#              'G', 'W', 'Y', 'B', 'V', 'K',
#              'X', 'J', 'Q', 'Z')
#
# letters22 = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R',
#              'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P',
#              'G', 'W', 'Y', 'B', 'V', 'K')

letters18 = ['A', 'S', 'E', 'T', 'N', 'I', 'O', 'R', 'H',
             'L', 'D', 'C', 'U', 'M', 'F', 'P',
             'G', 'W']

letters20 = ['A', 'S', 'E', 'T', 'N', 'I', 'O', 'R', 'H',
             'L', 'D', 'C', 'U', 'M', 'F', 'P',
             'G', 'W', 'Y', 'B']

letters8 = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R')

freq = get_freq_dict(get_data('data/freq_norvig.txt'))

key_weights = []

total_probability20 = sum(frequency for _, _, frequency in bigrams20)
# total_probability8 = sum(frequency for _, _, frequency in bigrams8)

if __name__ == '__main__':
    print(total_probability20)
    # print(total_probability8)
