# problem link: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/?child=first

def getFixedPayment(balance, annualInterestRate):
  # x is the initial balance
  x = balance
  payment = 10
  step = 10
  while balance > 0:
    balance = x
    payment += step
    for n in range(12):
      unpaid_balance = balance - payment
      balance = unpaid_balance + annualInterestRate / 12.0 * unpaid_balance

  print('Balance: ' + str(balance))
  print('Lowest Payment: ' + str(payment))
  return balance


getFixedPayment(3329, 0.2)