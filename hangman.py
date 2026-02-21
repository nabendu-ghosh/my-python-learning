import random

hangman_logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
'''
# Different stages of hangman drawing

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Predefined list of words for the game
word_list = ["morning", "journey", "weather", "kitchen", "picture",
    "balance", "freedom", "holiday", "morning", "outside",
    "payment", "quality", "respect", "silence", "traffic",
    "village", "warning", "victory", "student", "problem",
    "opinion", "natural", "message", "library", "justice",
    "history", "healthy", "fashion", "example", "evening",
    "culture", "country", "comfort", "brother", "believe",
    "airport", "ability", "account", "average", "benefit",
    "chicken", "display", "element", "failure", "general",
    "harvest", "imagine", "journal", "kitchen", "leather"]

# Variables for the gam
chosen_word = random.choice(word_list)
placeholder = ""
display = []
guessed_characters = []
lives = 6
win = False

# Game Starts
print(hangman_logo)

# Show the user number of characters in the word using underscores
for i in range(len(chosen_word)):
    placeholder += "_"
print (f"Word to guess: {placeholder}")

# Game Logic
while lives > 0:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    match = 0
    guess = input("Guess a letter: \t").lower()
    guessed_characters += guess

    if guess in placeholder:
        print(f"You have already guessed {guess}. Pick a different letter.")
        
    placeholder = list(placeholder)

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            placeholder[i] = guess
            match += 1

    placeholder = "".join(placeholder)

    if match == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
    if placeholder == chosen_word:
        win = True
        break
    print(stages[lives])
    print(f"Word to guess: {placeholder}")
    print(f"Guessed characters: {guessed_characters}")

if win:
    print(f"Congratulations! You win! The word was {chosen_word}")
else:
    print(f"Sorry, you lost! The word was {chosen_word}")