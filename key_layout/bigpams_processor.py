def calc_combs_sums(left_hand_combs, bigrams):
    comb_sum = []
    for left_hand_comb in left_hand_combs:
        sum_freq = calc_sum_freq(bigrams, left_hand_comb)
        comb_sum.append([left_hand_comb, sum_freq])
    return comb_sum


def calc_sum_freq(bigrams, left_hand_comb):
    sum_prob = 0
    for bigram in bigrams:
        if (bigram[0] in left_hand_comb) != (bigram[1] in left_hand_comb):
            sum_prob += bigram[2]
    return sum_prob




