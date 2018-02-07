def count7(N):
    remainder = N % 10
    integerPart = N // 10

    if integerPart == 0:
        if remainder == 7:
            return 1
        return 0
    else:
        if remainder == 7:
            return 1 + count7(integerPart)
        return 0 + count7(integerPart)

print(count7(747))