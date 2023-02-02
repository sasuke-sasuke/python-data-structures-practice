def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    idx = 0
    for item in lst:
        if (not not item) == False:
            lst.pop(idx)
        idx += 1
    return lst