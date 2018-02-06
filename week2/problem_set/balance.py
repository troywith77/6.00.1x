# problem link: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/?child=first

def getBalance(balance, yR, mR, m):
  if m == 0:
    return balance
  payment = balance * mR
  unpaid_balance = balance - payment
  b = unpaid_balance + yR / 12.0 * unpaid_balance
  return getBalance(b, yR, mR, m - 1)

print(getBalance(5000, 0.18, 0.02, 12))