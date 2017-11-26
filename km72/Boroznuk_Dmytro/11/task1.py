def GetN(): 
    '''
    This function recieves one integer from a user

    Args:
        -

    Returns:
        n - integer number (will be used in setList function)

    Raises:
        -

    Examples:
        >>> print(GetN())
        enter n <user_input>
        <user_input>

    '''
    global n
    while True:

        try:
            n=int(input('enter n '))
            break
        
        except ValueError:
            print('n - integer')
    

    return n
GetN()

def GetX():
    '''
    This function recieves one integer from a user

    Args:
        -

    Returns:
        x - float number (will be used in setList function)

    Raises:
        -

    Examples:
        >>> print(GetX())
        enter x <user_input>
        <user_input>

    '''
    global x
    while True:

        try:
            x=float(input('enter x '))
            break
        
        except ValueError:
            print('x - integer')
    

    return x
GetX()

def setlist(n,x):
    '''
    This function sets a list of results of an operation

    Args:
        n - integer number
        x - float number

    Returns:
        num_list - generated list of results of an operation (will be used in sumList function)

    Raises:
        -

    Examples:
        >>> print(setList(n,x))
        [<result1>, <result2> ... <resultn>]
    '''
    global num_list
    
    num_list=[]
    if n>=1:
        try:
            for i in range(1,n+1):
                a=float((x+i)/i)
                num_list.append(a)
      
        except ZeroDivisionError:
            print('0 division')
    else:
        print('n>=1')
    
    return num_list
setlist(n,x)

def sumList(num_list):
    '''
    This function sums the elements of the generated list

    Args:
        num_list - generated list of results of an operation

    Returns:
        sum - float number

    Raises:
        -

    Examples:
        >>> print(sumList([10, 12.5, -4])
        18.5
    '''
    sum=0
    for i in range(len(num_list)):
        sum=sum+num_list[i]
    return sum
print(sumList(num_list))
