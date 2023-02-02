def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq_dict1 = {}
    freq_dict2 = {}
    num1 = list(str(num1))
    num2 = list(str(num2))
    for num in num1:
        if num not in freq_dict1:
            freq_dict1[num] = 1
        else:
            freq_dict1[num] += 1
    for num in num2:
        if num not in freq_dict2:
            freq_dict2[num] = 1
        else:
            freq_dict2[num] += 1
    return freq_dict1 == freq_dict2