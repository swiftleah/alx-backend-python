#!/usr/bin/env python3
''' annotated function to_kv
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns tuple with 1st element as str k and 2nd element as
    square of int/float v '''
    return (k, float(v**2))
