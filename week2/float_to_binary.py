# 小数取余
# 先把小数乘以2**n变成整数，然后用整数转二进制的方法

x = 0.1
p = 0
while x * 2 ** p % 1 != 0:
  p += 1

x = int(x * 2 ** p)

result = ''
while x > 0:
  result = str(x % 2) + result
  x = x // 2

if p > len(result):
  # 补0
  result = (p - len(result)) * '0' + result

# result[0:-p] -> 去掉后p位
# result[-p:] -> 从后p位到最后
# 中间加'.'
result = result[0:-p] + '.' + result[-p:]
print(result)