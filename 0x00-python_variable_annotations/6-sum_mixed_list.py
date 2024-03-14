#!/usr/bin/env python3
''' annotated function sum_mixed_list
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' annotated function that takes mixed list of variables
    and returns sum of in form float '''
    return float(sum(mxd_lst))
