#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: Set containing elements present in only one of the sets.
    """
    return set_1.symmetric_difference(set_2)
