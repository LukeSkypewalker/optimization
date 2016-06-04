from common import *


def solve_it(input_data):

    items, capacity = get_items(input_data)
    print items

    nodes = [[0, 0, False, 0], [0, 0, True, 0]]
    counter = 0
    while len(nodes) != 0:
        counter += 1
        v, w, is_take, i = nodes.pop()
        print counter, i, is_take, v, w, items[i].value, items[i].weight

        if is_take:
            if (w + items[i].weight) > capacity:
                print '          overweight:', v, w
                continue
            v += items[i].value
            w += items[i].weight

        if i == len(items)-1:
            print '          ---leaf:', v, w
            continue

        nodes.append([v, w, False, i+1])
        nodes.append([v, w, True, i+1])

    print 'counter =', counter
    return


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    solve_it(get_data('./data/ks_4_0'))

