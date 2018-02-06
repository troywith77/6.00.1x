# a * b equals to add a for b times

def multi(a, b):
  result = 0
  while b > 0:
    result += a
    b -= 1
  return result

print(multi(12, 12))