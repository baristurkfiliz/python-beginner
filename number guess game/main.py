from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
life = 0
the_number = random.randint(1, 100)
win = False

def difficulty():
  global life
  diff = input("Choose a difficulty. Type 'easy' or 'hard'. : ")
  if diff == "easy":
    life = 10
  elif diff == "hard":
    life = 5
  else:
    print("Sorry. Invalid choise.")
    return difficulty

def main():
  global life
  global the_number
  global win
  guess = 0
  guess = int(input("Guess a number: "))
  while win == False:
    if guess <= the_number-1:
      print("It's too low")
      life -= 1
      print(f"Your guess ballance is {life}")
      if life == 0:
        print("You lose!")
        exit()
      else:
        main()
    elif guess >= the_number+1:
      print("It's too high")
      life -= 1
      print(f"Your guess ballance is {life}")
      if life == 0:
        print("You lose!")
        exit()
      else:
        main()
    else:
      print("You win!")
      win = True
      exit()

difficulty()
main()