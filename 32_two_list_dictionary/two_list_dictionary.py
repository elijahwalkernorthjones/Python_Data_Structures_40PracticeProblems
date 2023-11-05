def two_list_dictionary(keys, values):
    """Given keys and values, make a dictionary of those."""
    
    new_dictionary = {}

    for i in range(len(keys)):
        if i < len(values):
            new_dictionary[keys[i]] = values[i]
        else:
            new_dictionary[keys[i]] = None

    return new_dictionary

# Test cases
# print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
# print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
# print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
