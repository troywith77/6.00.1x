cube = 27
guess = 0.0
episilon = 0.01
increment = 0.01
num_guesses = 0

while abs(guess ** 3 - cube) >= episilon and guess <= cube:
  guess += increment
  num_guesses += 1

print('guessed ' + str(num_guesses) + ' times.')
if abs(guess ** 3 - cube) >= episilon:
  print('failed...')
else:
  print('the cude root of ' + str(cube) + ' is: ' + str(guess))

