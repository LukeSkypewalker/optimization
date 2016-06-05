from common import *


def solve_it(input_data):
    items, capacity = get_items(input_data)
    # print items

    taken = [0] * len(items)
    nodes = []
    nodes.append([0, 0, False, 0, list(taken)])
    nodes.append([0, 0, True, 0, list(taken)])
    best_set = [0, 0, taken]
    counter = 0
    while len(nodes) != 0:
        counter += 1
        v, w, is_take, i, taken = nodes.pop()
        # print counter, i, is_take, v, w, items[i].value, items[i].weight

        if is_take:
            if (w + items[i].weight) > capacity:
                if v > best_set[0]:
                    best_set = [v, w, taken]
                # print '   overweight:', v, w
                continue
            v += items[i].value
            w += items[i].weight
            taken[i] = 1

        if i == len(items) - 1:
            if v > best_set[0]:
                best_set = [v, w, taken]
            # print '   ---leaf:', v, w
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
