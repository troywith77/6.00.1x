def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    flag = a > b
    if flag:
        greater = a
    else:
        greater = b

    for n in range(1, greater):
        if a % n == 0 and b % n ==0:
            number = n
    if not number:
        number = 1
    return number

print(gcdIter(9, 16))