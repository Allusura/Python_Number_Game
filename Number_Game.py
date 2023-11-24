#Author: Allusura
#Description: A 'guessing' game where the console thinks of a number and the user has to guess it.

#Imports I will need for the project
import art
import random
import os

#Pre-defined 'lives' for the game.
EASY_LEVEL = 10
HARD_LEVEL = 5

#Function that welcomes the user to the game.
def welcome():
  os.system('clear')
  print(art.logo)
  print("\nWelcome to the Number Guessing Game!")
  print("\nI am thinking of a number between 1 and 100.")
  while True:
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy' or choice == 'hard':
      difficulty(choice)
      return False
    else:
        print(f"'{choice}' is not a valid input.")

#Function that decides what difficulty is chosen based on user input.
def difficulty(difficulty):
  if difficulty == 'easy':
    print("\nYou have 10 attempts remaining to guess the number.")
    game(10)
  else:
    print("\nYou have 5 attempts remaining to guess the number.")
    game(5)

#Function that has the actual game mechanics within it. 
def game(lives):
  computers_number = random.randint(1, 100)

  #While loop that keeps repeating while the user has enough lives remaining.
  while lives > 0:
    guess = int(input("\nMake a guess: "))
    
    if lives == 0:
      print(f"\nUnlucky. The number I was thinking of was: {computers_number}")
      break
    elif guess == computers_number:
      print(f"\nCongratulations! The number was {computers_number}.")
      print(f"You got it with {lives} lives left!\n")
      break
    elif guess > computers_number:
      lives -= 1
      if lives == 0:
        print(f"Unlucky, but you lose. The number I was thinking of, was {computers_number}")
        break
      print(f"The number I am thinking of is lower.\nYou have {lives} lives left.")
    elif guess < computers_number:
      lives -= 1
      if lives == 0:
        print(f"Unlucky, but you lose. The number I was thinking of, was {computers_number}")
        break
      print(f"The number I am thinking of is higher.\nYou have {lives} lives left.")

  #Calls the rematch function to ask if the user wants to try again
  rematch()

#Function used to see if the user wants to try again or not.
def rematch():

  try_again = input("Do you want to try again? Type 'y' for yes, and 'n' for no: ")
  if try_again == 'y':
    welcome()
  else:
    os.system('clear')
    print("Understandable, have a nice day.")
    
welcome()
