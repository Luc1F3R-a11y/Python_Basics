import random
random_number = random.randint(1, 100)

while True:
  user_input = int(input("Enter the number: "))
  if user_input < random_number:
    print("Too low! Try again.")
  elif user_input > random_number:
    print("Too high! Try again.")
  else:
    print("Congratulations! You guessed the number.")
    break