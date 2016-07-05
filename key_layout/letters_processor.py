def calc_letters_freq(letters, bigrams):
    return [(letter, calc_letter_freq_sum(letter, bigrams)) for letter in letters]


def calc_letter_freq_sum(letter, bigrams):
    return sum(b[2] for b in bigrams if letter in (b[0], b[1]))
    # return sum(b[2] for b in calc_letter_bigrams_freq(letter, bigrams))


def calc_letter_bigrams_freq(letter, bigrams):
    return [b for b in bigrams if letter in (b[0], b[1])]


if __name__ == '__main__':
    from key_layout.data import *

    letters_freq = calc_letters_freq(letters26, bigrams)
    letters_freq.sort(key=lambda x: x[1], reverse=True)
    print(*letters_freq, sep='\n')

    # data = [calc_letter_freq(letter, bigrams) for letter in letters26]
    # print(*data, sep='\n')

    # print(*(b[2] for b in calc_letter_freq('A', bigrams)), sep='\n')
