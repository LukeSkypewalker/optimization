def calc_combs_sums(letters, bigrams):
    data = []
    for letter in letters:
        sum_freq = calc_sum_freq(letter, bigrams)
        data.append([letter, sum_freq])
    return data


def calc_sum_freq(letter, bigrams):
    sum_prob = 0
    for bigram in bigrams:
        if letter in (bigram[0], bigram[1]):
            sum_prob += bigram[2]
    return sum_prob


def calc_letters_freq(letter, bigrams):
    data = []
    for bigram in bigrams:
        if letter in (bigram[0], bigram[1]):
            data.append(bigram)
    return data




if __name__ == '__main__':
    from key_layout.data import *

    # letters_freq = calc_combs_sums(letters, bigrams)
    # letters_freq.sort(key=lambda x: x[1], reverse=True)
    # print(*letters_freq, sep='\n')

    data = calc_letters_freq('B', bigrams)
    print(*data, sep='\n')

