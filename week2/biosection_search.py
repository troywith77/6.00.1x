square = 32178
start = 0
end = square
guess = 0
episilon = 0.01
num_guesses = 0

while abs(guess ** 2 - square) >= episilon:
  num_guesses += 1
  guess = (end + start) / 2.0
  print(guess, start, end)
  if guess ** 2 > square:
    print('end', guess)
    end = guess
  elif guess ** 2 < square:
    print('start', guess)
    start = guess
  else:
    break

print('guessed ' + str(num_guesses) + ' times.')
if abs(guess ** 2 - square) >= episilon:
  print('failed...')
else:
  print('the square root of ' + str(square) + ' is: ' + str(guess))