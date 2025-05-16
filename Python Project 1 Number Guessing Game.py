import random

name = input("Enter your name: ")

number_to_guess = random.randint(1, 100)
#Guesses numbers between 1 and 100
attempts = 0

while True :
    guess = int(input("Guess a number between 1 and 100: "))
    # Asks user to guess a number between 1 and 100
    attempts += 1
    # Increments the number of attempts by 1 each time the user guesses a number

    if guess == number_to_guess:
        print(f"Congratulations {name}! You guessed the correct number of {number_to_guess} in {attempts} attempts.")
        break  # Exit the loop once guessed correctly
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print(f"Sorry, the number was {number_to_guess}. Better luck next time!")