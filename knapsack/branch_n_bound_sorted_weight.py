from operator import attrgetter
from common import *


def solve_it(input_data):
    """
    >>> solve_it(get_data('./data/ks_4_0'))
    counter = 16
    [19, 11, [1, 0, 0, 1]]
    """

    items, capacity = get_items(input_data)
    items.sort(key=attrgetter('weight'), reverse=False)
    items_sorted = []
    for j, item in enumerate(items):
        items_sorted.append(Item(j, item.value, item.weight))

    # print items_sorted

    nodes = []
    taken = [0] * len(items_sorted)
    if items_sorted[0].weight <= capacity:
        nodes.append([0, 0, False, 0, list(taken)])
        nodes.append([0, 0, True, 0, list(taken)])

    best_set = [0, 0, taken]
    counter = 0

    while len(nodes) != 0:
        counter += 1
        v, w, is_take, i, taken = nodes.pop()
        # print counter, i, v, w, is_take, items[i].value, items[i].weight

        if is_take:
            v += items[i].value
            w += items[i].weight
            taken[i] = 1

        if i == len(items) - 1 or (w + items_sorted[i + 1].weight) > capacity:
            if v > best_set[0]:
                best_set = [v, w, taken]
            # print v, w
            continue

        nodes.append([v, w, False, i + 1, list(taken)])
        nodes.append([v, w, True, i + 1, list(taken)])

    print 'counter =', counter
    return best_set


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    best = solve_it(get_data('./data/ks_19_0'))
    print best
