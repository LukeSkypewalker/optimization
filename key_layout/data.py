from collections import namedtuple

Bigram = namedtuple("Bigram", ['a', 'b', 'frequency'])

from key_layout.data_helper import *

bigrams = get_bigrams_list(get_data('bigrams.txt'))
bigrams8 = get_bigrams_list(get_data('bigrams8.txt'))

letters26 = ('E', 'T', 'A', 'O', 'I', 'N', 'S', 'R',
             'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P',
             'G', 'W', 'Y', 'B', 'V', 'K',
             'X', 'J', 'Q', 'Z')

letters22 = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R',
             'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P',
             'G', 'W', 'Y', 'B', 'V', 'K')

letters8 = ('A', 'S', 'E', 'T', 'N', 'I', 'O', 'R')

efforts_4 = [[0, 0.9, 0.75, 0.8],
             [0.8,  0,    0.9,   0.85],
             [0.8,  0.9,  0,     2.5 ],
             [0.8,  0.8,  1,     0   ]]

#               |1    |2    |3   |4      |5     |6     |7   |8     |9   |10
efforts_full = [[0,    0.85, 0.8, 0.85,   0.5,   0.6,   0.1, 0.2,   0.2, 0.3],  # 1
                [0.8,  0,    1.2, 0.9,   -1.0,   1.1,   0.2, 0.4,   0.3, 0.2],  # 2
                [0.8,  0.9,  0,   1.5,    0.7,  -0.5,  -0.5, 0.4,   0.2, 0.1],  # 3
                [0.85, 0.8,  1.0, 0,      0.75,  0.9,   0.2, -0.5, -0.6, -0.6],  # 4
                [0.75, -1.0, 0.7, 0.7,    0,     0.6,  -0.4, 0.1,   0.4, 0.1],  # 5
                [0.75, 0.4, -0.5, 1.1,    0.5,   0,    -0.6, 0.2,   0.4, 0.1],  # 6 +
                [0.4,  0.3, -0.5, 0.4,   -0.6,  -1.0,   0,   0.7,  -0.5, 0.1],  # 7 +
                [0.6,  0.4,  0.6, -0.5,   0.3,   0.3,   0.5, 0,    -0.9, -1.0],  # 8
                [0.5,  0.4,  0.4, -0.6,   0.4,   0.5,  -0.5, -1.0,  0,   -1.0],  # 9
                [0.3,  0.1,  0.1, -1.0,   0.3,   0.1,   0.1, -1.0, -1.0, 0]]  # 10

key_weights = []

total_probability = sum(frequency for _, _, frequency in bigrams)
total_probability8 = sum(frequency for _, _, frequency in bigrams8)

if __name__ == '__main__':
    print(total_probability)
    print(total_probability8)
