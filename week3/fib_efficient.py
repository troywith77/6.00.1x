def fib_efficient(n, d):
  if n in d:
    return d[n]
  ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
  d[n] = ans
  return ans

print(fib_efficient(5, { 1: 1, 2: 1 }))