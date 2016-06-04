#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import greed_sorted_by_density as greed
from common import get_data


def solve_it(input_data):
    return greed.solve_it(input_data)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'
