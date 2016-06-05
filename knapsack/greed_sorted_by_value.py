from operator import attrgetter
from common import *


def solve_it(input_data):
    """
    >>> solve_it(get_data('./data/ks_4_0'))
    '19 0\\n0 0 1 1'
    >>> solve_it(get_data('./data/ks_19_0'))
    '12066 0\\n0 0 1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0'
    """
    items, capacity = get_items(input_data)
    items.sort(key=attrgetter('value'), reverse=True)

    value = 0
    weight = 0
    taken = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import doctest

    doctest.testmod()
