from datetime import datetime

from common import *
import numpy as np


def solve_it(input_data):
    items, capacity = get_items(input_data)

    matrix = dynamic_programming(capacity, items)
    taken = restore_taken(matrix, items)
    total_value = matrix[-1][-1]
    # total_weight = sum([item.weight * taken[i] for i, item in enumerate(items)])
    # print total_weight

    output_data = convert_answer(total_value, taken, is_optimal=False)
    return output_data


def dynamic_programming(capacity, items):
    m = np.zeros((capacity + 1, len(items) + 1), dtype=int)
    for i, item in enumerate(items):
        i += 1
        for cap in range(1, capacity + 1):
            x = m[cap - item.weight, i - 1] if cap - item.weight >= 0 else 0
            y = item.value if item.weight <= cap else 0
            m[cap, i] = max(m[cap, i - 1], x + y)
    # print m
    return m


def restore_taken(matrix, items):
    n = len(matrix) - 1
    m = len(matrix[0]) - 1
    taken = [0] * m
    # print n, m, taken
    for i in range(m, 0, -1):
        if matrix[n][i] != matrix[n][i - 1]:
            taken[i - 1] = 1
            n -= items[i - 1].weight
    return taken


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    start = datetime.now()
    res = solve_it(get_data('./data/ks_100_0'))
    end = datetime.now()

    print res
    print end - start
