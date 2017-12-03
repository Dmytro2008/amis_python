a = input("Введите последовательность натуральных чисел:").split()
def secondvalue(a):
    """
    This function is calculating the value of the second largest element

    Args:
        a: list, which contains natural numbers
    Returns:
        a: the second largest element
    Raises:
        ValueError
    Examples:
        print(secondvalue(21,54,15,3)
        21
        print(secondvalue(21,54)
        ValueError: min() arg is an empty sequence
    """
    a.remove(min(a))
    if len(a) == 2:
        a.remove(max(a))
        return "".join(a)
    else:
        return(secondvalue(a))
print(secondvalue(a))
