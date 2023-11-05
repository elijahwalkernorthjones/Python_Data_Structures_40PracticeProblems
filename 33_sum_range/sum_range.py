def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0

    # Determine the starting and ending indices based on the parameters
    start_idx = nums.index(start) if start in nums else 0
    end_idx = nums.index(end) if end in nums else len(nums)

    # Iterate through the list and calculate the sum
    for i in range(start_idx, end_idx):
        sum += nums[i]

    return sum