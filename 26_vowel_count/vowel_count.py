def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    letterDict = {}
    vowels = "aeiouAEIOU"
   
    for letter in phrase:
        letter = letter.lower()
        if letter in vowels:
            if letter in letterDict:
                letterDict[letter] +=1
            else :
                letterDict[letter] = 1

    return letterDict