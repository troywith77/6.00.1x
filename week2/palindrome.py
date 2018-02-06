def isPalindrome(str):
  print(str)
  if len(str) <= 1:
    return True
  return str[0] == str[-1] and isPalindrome(str[1:-1])

print(isPalindrome('abcba'))