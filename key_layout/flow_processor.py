from datetime import datetime

from key_layout.data.data import bigrams


# TODO: +++from right to G
# TODO: 22 letters ?

#       |1     |2     |3    |4     |5     |6    |7    |8    |9    |10
flow = [[0,     0.9,   0.8,  0.85,  0.7,   0.6,  0.1,  0.2,  0.1,  0.2],  # 1
        [0.8,   0,     1.2,  0.9,  -1.0,   1.2,  0.2,  0.4,  0.2,  0.1],  # 2
        [0.8,   0.9,   0,    2,     0.7,  -0.5, -0.5,  0.4,  0.2,  0.1],  # 3
        [0.85,  0.8,   1.0,  0,     0.75,  0.9,  0.2, -0.5, -0.6, -0.6],  # 4
        [0.75, -1.0,   0.7,  0.7,   0,     0.6, -0.4,  0.1,  0.4,  0.1],  # 5
        [0.75,  0.4,  -0.5,  1.1,   0.5,   0,   -0.6,  0.2,  0.4,  0.1],  # 6
        [0.4,   0.3,  -0.5,  0.4,  -0.6,  -1.0,  0,    0.7, -0.5,  0.1],  # 7
        [0.6,   0.4,   0.6, -0.5,   0.3,   0.3,  0.5,  0,   -0.9, -1.0],  # 8
        [0.5,   0.4,   0.4, -0.6,   0.4,   0.5, -0.5, -1.0,  0,   -1.0],  # 9
        [0.3,   0.1,   0.1, -1.0,   0.3,   0.1,  0.1, -1.0, -1.0,  0  ]]  # 10

alpha = 1


def calc_hand_flow(hand):
    """
    >>> calc_hand_flow(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'])
    2983832436.200001
    >>> calc_hand_flow(['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    2803440215.7999997
    """

    flow_score = 0
    for b in bigrams:
        if b[0] == b[1]:
            continue

        k = 0
        if (b[0] in hand) != (b[1] in hand):
            k = 1
        if (b[0] in hand) and (b[1] in hand):
            i = hand.index(b[0])
            j = hand.index(b[1])
            k = flow[i][j] * alpha
            # print(b, i, j, k)

        # print(b, k)
        flow_score += b[2] * k
    return flow_score


def calc_layout_flow(left, right):
    """
    >>> calc_layout_flow(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'],
    ...                  ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    5787272652
    """

    layout_score = calc_hand_flow(left) + calc_hand_flow(right)
    return round(layout_score)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    time_start = datetime.now()
    res = calc_hand_flow(aest)
    time_end = datetime.now()
    print('flow_left', res)
    print('time', time_end - time_start)

    res = calc_hand_flow(niro)
    print('flow_right', res)

    layout_flow = calc_layout_flow(aest, niro)
    print('layout flow', layout_flow)
