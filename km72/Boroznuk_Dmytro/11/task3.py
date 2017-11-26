def getnumber():
    Num = input("Enter number of elements in list: ")
    """
    This function is checking data(data must be int)

    Args:
        Function takes no args
    Returns:
        a - integer, will be used in function "calculating"
        A string, that give information about data (correct ot no)
    Raises:
        OverflowError
    Examples:
        print(getnumber())
        (if we enter 100)
        Data is correct
        100
        print(getnumber())
        (if we enter abc)
        Enter natural digit
        (if we enter 101)
        Data is correct
        101
        """
    if Num.isdigit() == False:
        print("Enter natural digit")
        return getnumber()
    if len(Num) < 1:
        print("Enter natural digit")
        return getnumber()
    else:
        if int(Num) <= 0:
            print("Number of multiplying can't be < 0.")
            return getnumber()
        else:
            print("Data is correct")
    return int(Num)
Num = getnumber()
digits = []


def getlist(Num):
    """
    This function is creating list
    Args:
        Num: integer, number of repeating
    Returns:
        list: list, list of digits
    Raises:
        OverflowError
    Examples:
        print(getlist())
        (if we enter 1,2,3,4,5)
        [1,2,3,4,5]"""
    global digits
    if len(digits) < Num:
        a = int(input("Enter element: "))
        digits.append(a)
        getlist(Num)
    else:
        return digits
    return digits
list = getlist(Num)
res = []
it = 1


def convert_list(list, it):
    """
    This function is reversing list

    Args:
        list: list, which is reversing
        it: integer, iterator, that points on element in list
    Returns:
        res: reversed list
    Raises:
        OverflowError
        ValueError
    Examples:
        print(min_f([1,2,3,4],0))
        [4,3,2,1]
        print(min_f([1,2,"a",3],0))
        ValueError"""
    global res
    if len(list) == it-1:
        return res
    res.append(list[it])
    return convert_list(list, it+1)
print(convert_list(list, it))
