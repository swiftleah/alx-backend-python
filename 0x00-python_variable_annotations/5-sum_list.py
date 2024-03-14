#!/usr/bin/env python3
''' annotated function sum_list
'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' function takes floats and returns sum as float
    '''
    return float(sum(input_list))
