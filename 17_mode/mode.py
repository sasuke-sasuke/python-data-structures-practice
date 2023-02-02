def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common_dict = {}
    for num in nums:
        if num not in most_common_dict:
            most_common_dict[num] = 1
        else:
            most_common_dict[num] += 1
    winner = None
    value = None
    for k, v in most_common_dict.items():
        if winner == None:
            winner = k
            value = v
        elif v > value:
            winner = k
            value = v
    return winner


