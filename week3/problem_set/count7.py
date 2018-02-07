def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    # 将数字转成字符串
    t = str(N)
    length = len(t)
    print('N: ' + t)

    # 如果为空字符串，返回0
    if not t:
        return 0

    # 如果第一位转成整型后等于7，则返回1
    if int(t[0]) == 7:
        n = 1
    else:
        n = 0

    # 如果字符串只有一位了，停止递归
    if length == 1:
        return n
    # 否则返回n加上当前字符串index后面的count7递归调用
    else:
        return n + count7(int(t[1:]))

print(count7(1237123))