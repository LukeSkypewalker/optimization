import numpy as np

def tst():
    m = np.zeros((2, 3), dtype=int)
    m[1][1]=1
    print m
    return m


if __name__ == '__main__':

    n = tst()
    print n