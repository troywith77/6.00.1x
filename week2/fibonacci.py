def fib(n):
  if n == 0 or n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))