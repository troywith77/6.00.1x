# problem link: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/

# bisection search

def getFixedPayment(balance, annualInterestRate):
  # x is the initial balance
  x = balance
  low = balance / 12.0
  high = balance * (1 + annualInterestRate) ** 12 / 12.0
  payment = (high + low) / 2
  num_iterates = 0

  while abs(balance) > 0.1:
    balance = x
    payment = (high + low) / 2
    num_iterates += 1
    for n in range(12):
      unpaid_balance = balance - payment
      balance = unpaid_balance + annualInterestRate / 12.0 * unpaid_balance
    if balance > 0:
      low = payment
    elif balance < 0:
      high = payment
    else:
      break

  print('Iterated ' + str(num_iterates) + ' times.')
  print('Lowest Payment: ' + str(round(payment, 2)))
  return balance


getFixedPayment(999999, 0.18)