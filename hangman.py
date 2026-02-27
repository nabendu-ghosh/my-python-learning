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
word_list = [
    # 4 Letters
    "atom", "blue", "bolt", "cave", "dark", "dust", "fire", "gate", 
    "iron", "leaf", "luck", "moon", "rain", "star", "wind", "wolf",
    
    # 5 Letters
    "alarm", "beach", "brain", "candy", "dance", "eagle", "fruit", "glass", 
    "heart", "light", "music", "night", "party", "river", "smile", "tower",
    
    # 6 Letters
    "bridge", "camera", "castle", "desert", "energy", "forest", "guitar", "island", 
    "market", "museum", "planet", "rocket", "shadow", "silver", "spirit", "winter",
    
    # 7 Letters
    "ancient", "blanket", "channel", "diamond", "feather", "gravity", "horizon", "journey", 
    "lantern", "mystery", "octopus", "pyramid", "science", "thunder", "unknown", "volcano",
    
    # 8 Letters
    "birthday", "champion", "daughter", "elephant", "fountain", "hospital", "interest", "language", 
    "mountain", "neighbor", "platform", "question", "sandwich", "treasure", "umbrella", "vacation",
    
    # 9+ Letters
    "architecture", "celebration", "discovery", "education", "furniture", "happiness", "imagination", "landscape", 
    "nightmare", "operation", "passenger", "reflection", "satellite", "telephone", "universe", "yesterday"
]

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