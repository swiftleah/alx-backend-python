#!/usr/bin/env python3
''' augmenting given code
'''


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''augmenting function for any kind of elements
    '''
    if lst:
        return lst[0]
    else:
        return None
