from key_layout.data import *


def calc_letters_freq(letters, bigrams):
    return [(letter, calc_letter_freq(letter, bigrams)) for letter in letters]


def calc_letter_freq(letter, bigrams):
    """
    >>> calc_letter_freq('E', bigrams)
    1031369703
    >>> calc_letter_freq('A', bigrams)
    739408216
    """
    return sum(b[2] for b in get_all_letters_bigrams(letter, bigrams))
    # return sum(b[2] for b in bigrams if letter in (b[0], b[1]))


def get_all_letters_bigrams(letter, bigrams):
    return [b for b in bigrams if letter in (b[0], b[1])]


def get_bigram_list_summarized(_letter, bigrams):
    data = get_all_letters_bigrams(_letter, bigrams)
    bidirect_digrams = []
    for letter in letters26:
        if letter == _letter:
            continue
        bs = ([b for b in data if letter in (b[0], b[1])])
        bsum = round(sum([b[2] for b in bs]) / 1000)
        bidirect_digrams.append([letter, bsum, bs])

    bidirect_digrams.sort(key=lambda x: x[1], reverse=True)
    return bidirect_digrams


if __name__ == '__main__':
    from key_layout.data import *
    import doctest

    doctest.testmod()

    # check letters frequencies
    # letters_freq = calc_letters_freq(letters26, bigrams)
    # letters_freq.sort(key=lambda x: x[1], reverse=True)
    # print(*letters_freq, sep='\n')

    # data = get_all_letters_bigrams('A', bigrams)
    # data.sort(key=lambda x: x[2], reverse=True)
    # print(*(data), sep='\n')

    data = [get_bigram_list_summarized(letter, bigrams) for letter in letters26]
    from pprint import pprint
    pprint(data)
