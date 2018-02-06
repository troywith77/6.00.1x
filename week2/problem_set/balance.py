# problem link: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/?child=first

def getBalance(balance, annualInterestRate, monthlyPaymentRate, m = 12):
  if m == 0:
    print('Remaining balance: ' + str(round(balance, 2)))
    return balance
  payment = balance * monthlyPaymentRate
  unpaid_balance = balance - payment
  b = unpaid_balance + annualInterestRate / 12.0 * unpaid_balance
  return getBalance(b, annualInterestRate, monthlyPaymentRate, m - 1)

getBalance(42, 0.2, 0.04)