user_list = input("Enter your list: ").split()
empty_list = []
def func(list, iterator):
    """
    This function is counting group of elements
    Args:
        list: list with natural numbers
        iterator: integer number, iterator
    Returns:
        max number of elements in "group"
    Raises:
        ValueError
    Examples:
        >>>print(func([5, 5, 5, 1, 7, 4], 0))
        3
        
        >>>print(func([7, 7, s, 8, 8, 5,6], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if iterator == len(list):
        return max(empty_list)
    list2 = "".join(list)
    count_el = list.count(list[iterator])
    if (count_el - iterator)*str(list[iterator]) in list2:
        empty_list.append(count_el - iterator)
    return func(list, iterator + 1)
print(func(user_list, 0))
