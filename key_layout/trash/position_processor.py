from pprint import pprint

# TODO:
from key_layout.hand_permutations import get_smart_permutations_right

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    pprint(get_smart_permutations_right(aest))