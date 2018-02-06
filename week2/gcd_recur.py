# 终于对递归有感觉了
# gcd(a, b) === gcd(b, a % b)
# a > b

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    flag = a > b
    if flag:
        high = a
        low = b
    else:
        high = b
        low = a
    print('gcd(' + str(high) + ', ' + str(low) + ')')
    if low == 0:
      return high
    return gcdRecur(low, high % low)


print(gcdRecur(9, 12))