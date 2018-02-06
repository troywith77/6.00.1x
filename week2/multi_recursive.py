def multi(a, b):
  if b == 1:
    return a
  return a + multi(a, b - 1)

print(multi(13, 13))