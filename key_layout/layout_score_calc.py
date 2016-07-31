from key_layout.balance_processor import calc_disbalance
from key_layout.flow_processor import calc_layout_flow


def calc_score(layout):
    """
    >>> calc_score(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B',
    ...             'O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    488583592.401858
    """

    n = len(layout) // 2
    left = layout[0:n]
    right = layout[n:]

    flow = calc_layout_flow(left, right)
    disbalance = calc_disbalance(left, right)

    score = flow / disbalance
    return score
