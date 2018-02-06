# 先除以2取余加一位，然后除以2的整数位继续取余直到数除以2取整数位小于0

num = 19
result = ''

if num < 0:
  isNeg = True
  num = -num
else:
  isNeg = False

while num > 0:
  result = str(num % 2) + result
  num = num // 2

result = int(result)
if isNeg:
  result = -result

print(result)