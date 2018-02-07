def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    # 除以10取余获得最后一位数字
    remainder = N % 10
    # 除以10取整获得去掉最后一位数字的新数字
    integerPart = N // 10

    # 如果数字只有一位数就返回当前数字
    if integerPart == 0:
        return N
    # 否则返回去掉的一位数加上当前数字取sum的递归函数
    return remainder + sumDigits(integerPart)

print(sumDigits(21))