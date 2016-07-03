from collections import namedtuple
from operator import attrgetter
from common import *

Best_set = namedtuple("Best_set", ['value', 'weight', 'taken'])


def estimate_max_value(items, capacity):
    """
    >>> test_items = [Item(index=0, value=10, weight=5), Item(index=1, value=8, weight=4), Item(index=2, value=15, weight=8), Item(index=3, value=4, weight=3)]
    >>> estimate_max_value(test_items, 11)
    21.75
    """

    value = 0
    weight = 0
    for item in items:
        if weight + item.weight <= capacity:
            value += item.value
            weight += item.weight
        else:
            remain_capacity = capacity - weight
            fraction_value = item.value * (remain_capacity / float(item.weight))
            value += fraction_value
            break
    return value


def solve_it(input_data):
    """
    >>> solve_it(get_data('./data/ks_4_0'))
    counter = 20
    [19, 11, [0, 0, 1, 1]]
    """

    items, capacity = get_items(input_data)
    items.sort(key=lambda x: (x.value / float(x.weight), x.value), reverse=True)
    items_sorted = []
    for j, item in enumerate(items):
        items_sorted.append(Item(j, item.value, item.weight))

    # print items_sorted

    taken = [0] * len(items_sorted)
    nodes = []
    nodes.append([0, 0, False, 0, list(taken)])
    nodes.append([0, 0, True, 0, list(taken)])

    best_set = Best_set(0, 0, taken)
    counter = 0

    while len(nodes) != 0:
        counter += 1
        v, w, is_take, i, taken = nodes.pop()
        # print counter, i, v, w, is_take, items[i].value, items[i].weight

        if is_take and (w + items_sorted[i].weight) <= capacity:
            v += items[i].value
            w += items[i].weight
            taken[i] = 1

        if v > best_set[0]:
            best_set = [v, w, taken]

        if i == len(items) - 1:
            # print v, w
            continue

        max_remain_value = estimate_max_value(items[i + 1:], capacity - w)
        if best_set[0] >= v + max_remain_value:
            # print 'pruned', best_set[0], '>', bound
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
