print("Please think of a number between 0 and 100!")

flag = False
low = 0
high = 100

while not flag:
  guess = (high + low) // 2
  print('Is your secret number ' + str(guess) + '?')
  user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  if user_inp == 'h':
    high = guess
  elif user_inp == 'l':
    low = guess
  elif user_inp == 'c':
    flag = True
  else:
    print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))