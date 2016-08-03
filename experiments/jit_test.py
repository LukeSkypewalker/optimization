import timeit

import numpy as np
import numba as nb


def f_with_return(n):
    k = 0.
    for i in range(n):
        for j in range(n):
            k += i + j
    return k


jit_f_with_return = nb.jit()(f_with_return)
jit_f_with_return_nopython = nb.jit(nopython=True)(f_with_return)

print(timeit.timeit('f_with_return(1000)', setup="from __main__ import f_with_return", number=100))
print(timeit.timeit('jit_f_with_return(1000)', setup="from __main__ import jit_f_with_return", number=100))
print(timeit.timeit('jit_f_with_return_nopython(1000)', setup="from __main__ import jit_f_with_return_nopython", number=100))
