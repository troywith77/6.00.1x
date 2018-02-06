"""
We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.
"""

def isIn(char, aStr):
  # 如果字符串为空，return False
  if not aStr:
    return False
  # 取到中间一个char
  length = len(aStr)
  index = int(round(length / 2.0))
  middle = aStr[index - 1]
  # 比对中间一个char和指定char是否相等
  if length == 1:
    return char == aStr[0]
  if middle == char:
    return True
  # 如果比中间数大，去右边
  elif (char > middle):
    return isIn(char, aStr[index:])
  # else，去左边
  return isIn(char, aStr[:index])

print(isIn('s', 'bbddefgggilnptvy'))
