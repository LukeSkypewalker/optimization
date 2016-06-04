from operator import attrgetter
from common import *


def solve_it(input_data):
    """
    >>> solve_it(get_data('./data/ks_4_0'))
    pruned: 12 7
    pruned: 14 8
    leaf: 19 11
    leaf: 4 3
    pruned: 18 9
    pruned: 8 4
    pruned: 10 5
    leaf: 15 8
    leaf: 0 0
    counter = 16
    """

    items, capacity = get_items(input_data)
    items.sort(key=attrgetter('weight'), reverse=False)
    items_sorted = []
    for j, item in enumerate(items):
        items_sorted.append(Item(j, item.value, item.weight))

    # print items_sorted

    nodes = []
    if items_sorted[0].weight <= capacity:
        nodes.append([0, 0, False, 0])
        nodes.append([0, 0, True, 0])

    counter = 0
    # for i, item in enumerate(items_sorted):
    while len(nodes) != 0:
        counter += 1
        v, w, is_take, i = nodes.pop()
        # print counter, i, v, w, is_take, items[i].value, items[i].weight

        if is_take:
            v += items[i].value
            w += items[i].weight

        if i == len(items)-1:
            print 'leaf:', v, w
            continue

        if (w + items_sorted[i + 1].weight) > capacity:
            print 'pruned:', v, w
            continue

        nodes.append([v, w, False, i + 1])
        nodes.append([v, w, True, i + 1])

    print 'counter =', counter
    return


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    solve_it(get_data('./data/ks_4_0'))
