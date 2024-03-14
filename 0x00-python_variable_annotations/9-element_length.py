#!/usr/bin/env python3
'''annotated function  element_length
'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''computes length of list of sequences
    '''
    return [(i, len(i)) for i in lst]
