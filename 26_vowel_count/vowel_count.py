def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_count = {}
    vowels = 'aeoiu'
    for char in phrase:
        char = char.lower()
        if char not in vowel_count and char in list(vowels):
            vowel_count[char] = 1
        elif char in list(vowels):
            vowel_count[char] += 1
    return vowel_count