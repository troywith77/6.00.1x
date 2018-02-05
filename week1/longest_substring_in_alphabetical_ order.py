# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

# 字母表
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# 字母表长度
alphabetLength = len(alphabet)
s = 'kqzopdsvvuvoxwdgseviijpe'
sLength = len(s)
# 符合顺序的所有substring
arr = []
# 循环字符串s
for i in range(sLength):
  str = s[i]
  # 从当前项目的下一个开始另一个循环
  for j in range(i + 1, sLength):
    # 如果下一个str在字母表中的index大于等于上一个str在字母表中的index，证明在上一个字母后面或相等，相加之后继续判断下下个项目
    # 否则停止循环
    if (alphabet.index(s[j]) >= alphabet.index(s[j - 1])):
      str += s[j]
    else:
      break
  if len(str) > 1:
    arr.append(str)
largestIndex = 0
largestLength = 0
# 在所有符合顺序的字符串中找到最先出现的最长的
for n in range(len(arr)):
  if len(arr[n]) > largestLength:
    largestIndex = n
    largestLength = len(arr[n])
largestStr = arr[largestIndex]
print('Longest substring in alphabetical order is: ' + largestStr)
