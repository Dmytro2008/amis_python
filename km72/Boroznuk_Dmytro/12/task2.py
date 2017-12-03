a = input("Введите последовательность натуральных чисел:").split()
q = (len(a)-1)
counter = 0
def quantitymaxs(a,q):
    """
    This function counts quantity of maximal elements

    Args:
        a: list, which contains natural numbers
        q: integer, iterator, that points on element in list
    Returns:
        counter: integer, quantity of maximal elements
    Raises:
        -
    Examples:
        print(quantitymaxs(2,3,56,56,44,q))
        2
        print(quantitymaxs(5,5,4,5,2,q))
        3"""
    global counter
    if a[q] == max(a):
        counter += 1
    if q == 0:
        return counter
    if q != 0:
        return quantitymaxs(a,q-1)
print(quantitymaxs(a,q))
