def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letterDict = {}
    for letter in phrase:
        letter = letter.lower()

        if letter in letterDict:
            letterDict[letter] +=1
        else :
            letterDict[letter] = 1

    return letterDict