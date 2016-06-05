from operator import attrgetter
from common import *



def get_max_bound(i, items, value, weight, capacity):
    """
    >>> test_items = [Item(index=0, value=10, weight=5), Item(index=1, value=8, weight=4), Item(index=2, value=15, weight=8), Item(index=3, value=4, weight=3)]
    >>> get_max_bound(0, test_items, 10, 5, 11)
    21.75
    >>> get_max_bound(0, test_items, 0, 0, 11)
    21.125
    >>> get_max_bound(2, test_items, 0, 0, 11)
    4
    >>> get_max_bound(100, test_items, 0, 0, 11)
    0
    """

    items_remain = items[i:]

    items_remain.sort(key=lambda x: (x.value / float(x.weight), x.value), reverse=True)
    items_sorted = []
    for j, item in enumerate(items_remain):
        items_sorted.append(Item(j, item.value, item.weight))

    # print i, items_sorted

    i = 0
    while i < len(items_sorted) - 1:
        i += 1
        if capacity >= weight + items_sorted[i].weight:
            weight += items_sorted[i].weight
            value += items_sorted[i].value
        else:
            free_weight = capacity - weight
            fraction_value = items_sorted[i].value * (free_weight / float(items_sorted[i].weight))
            value += fraction_value
            break
    return value


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

        bound = get_max_bound(i, items, v, w, capacity)
        if best_set[0] >= bound:
            # print 'pruned', best_set[0], '>', bound
            continue

        nodes.append([v, w, False, i + 1, list(taken)])
        nodes.append([v, w, True, i + 1, list(taken)])

    print 'counter =', counter
    return best_set


if __name__ == '__main__':
    import doctest

    # doctest.testmod()

    best = solve_it(get_data('./data/ks_30_0'))
    print best
