from datetime import datetime

from key_layout.data.data import bigrams

# TODO: +++from right to G
# TODO: 20 or 22 letters ?

#       |1     |2     |3    |4     |5     |6    |7    |8    |9    |10
flow = [[0,     0.9,   0.8,  0.85,  0.7,   0.6,  0.1,  0.2,  0.1,  0.2],  # 1
        [0.8,   0,     1.2,  0.9,  -1.0,   1.1,  0.2,  0.4,  0.2,  0.1],  # 2
        [0.8,   0.9,   0,    3,     0.7,  -0.6, -0.5,  0.4,  0.2,  0.1],  # 3
        [0.85,  0.8,   1.0,  0,     0.75,  0.9,  0.2, -0.5, -0.6, -0.6],  # 4
        [0.75, -1.0,   0.7,  0.7,   0,     0.6, -0.4,  0.1,  0.4,  0.1],  # 5
        [0.75,  0.4,  -0.5,  1.1,   0.5,   0,   -0.6,  0.2,  0.4,  0.1],  # 6
        [0.4,   0.3,  -0.5,  0.4,  -0.6,  -1.0,  0,    0.7, -0.5,  0.1],  # 7
        [0.6,   0.4,   0.6, -0.5,   0.3,   0.3,  0.5,  0,   -0.9, -1.0],  # 8
        [0.5,   0.4,   0.4, -0.6,   0.4,   0.5, -0.5, -1.0,  0,   -1.0],  # 9
        [0.3,   0.1,   0.1, -1.0,   0.3,   0.1,  0.1, -1.0, -1.0,  0  ]]  # 10

alpha = 1


def calc_flow(hand):
    """
    >>> calc_flow(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'])
    3032801814.200001
    >>> calc_flow(['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    2890756278.8999996
    """

    flow_score = 0
    for b in bigrams:
        if b[0] == b[1]:
            continue

        is_b0_in_hand = b[0] in hand
        is_b1_in_hand = b[1] in hand

        if not is_b0_in_hand and not is_b1_in_hand:
            continue

        if is_b0_in_hand and is_b1_in_hand:
            i = hand.index(b[0])
            j = hand.index(b[1])
            k = flow[i][j] * alpha
        else:
            k = 1

        # print(b, k)
        flow_score += b[2] * k
    return flow_score


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    time_start = datetime.now()
    res = calc_flow(aest)
    time_end = datetime.now()
    print('flow_left', res)
    print('time', time_end - time_start)

    # res = calc_flow(niro)
    # print('flow_right', res)
