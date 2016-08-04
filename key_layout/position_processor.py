from datetime import datetime
from pprint import pprint

from key_layout.data.data import bigrams


# TODO:
from key_layout.hand_permutations import get_smart_permutations

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    pprint(get_smart_permutations(aest))