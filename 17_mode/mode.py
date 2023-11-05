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
    # Create a dictionary to store the count of each number
    num_count = {}

    # Iterate through the list and count occurrences
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Find the mode by iterating through the dictionary
    mode_value = None
    max_count = 0

    for num, count in num_count.items():
        if count > max_count:
            max_count = count
            mode_value = num

    return mode_value
