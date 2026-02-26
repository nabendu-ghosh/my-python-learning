import random

game_logo = r'''
    ______                      __  __            
  / ____/_  _____  __________ / /_/ /_  ___      
 / / __/ / / / _ \/ ___/ ___// __/ __ \/ _ \     
/ /_/ / /_/ /  __(__  |__  )/ /_/ / / /  __/     
\____/\__,_/\___/____/____/ \__/_/ /_/\___/      
    _   __                __                     
   / | / /_  ______ ___  / /_  ___  _____        
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/        
 / /|  / /_/ / / / / / / /_/ /  __/ /            
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/
'''
welcome_message = "Welcome to the Number Guessing Game!"
lives = -1

print(game_logo)
print(welcome_message)
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
    lives = 10
elif difficulty_level == "hard":
    lives = 5
else:
    print("Please enter either 'easy' or 'hard'")

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number")
    
    if lives == 1:
        print(f"This is your last attempt!")

    guessed_number = int(input("Make a guess: "))

    if guessed_number == number:
        print(f"You guessed it correctly. The number was: {number}")
        break
    elif guessed_number > number:
        print("Too high")
    else:
        print("Too low")
    lives -= 1

if lives == 0:
    print(f"You lose. The correct no was:{number}.Please try again.")

