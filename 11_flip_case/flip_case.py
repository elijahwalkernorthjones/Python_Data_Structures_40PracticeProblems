def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = ''
    for char in phrase:
        if char.isupper() and char.lower() == to_swap.lower():
            flipped_phrase += char.lower()
        elif char.islower() and char.lower() == to_swap.lower():
            flipped_phrase += char.upper()
        else:
            flipped_phrase += char
    return flipped_phrase
            


    # if to_swap.isupper() == True:
    #     #then swap that character to lower and append
    # elif to_swap.islower() == True:
    #     #then swap that character to upper and append
    # else :
    #     #append that character to string