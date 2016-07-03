from collections import namedtuple
Bigram = namedtuple("Bigram", ['a', 'b', 'frequency'])

from key_layout.data_helper import *
bigrams = get_bigrams_list(get_data('bigrams.txt'))

# letters = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R',
#            'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P',
#            'G', 'W', 'Y', 'B', 'V', 'K',
#            'X', 'J', 'Q', 'Z')

letters = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R',
           'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P',
           'G', 'W', 'Y', 'B', 'V', 'K')

# letters = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R')

total_probability = sum(frequency for _, _, frequency in bigrams)


if __name__ == '__main__':
    print(total_probability)