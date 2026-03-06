import random
from higher_lower_data import game_data, game_logo, vs_logo

def pick_account(accounts_list: list):
    '''
    Takes the accounts in a list form and returns a random account
    '''
    return random.choice(accounts_list)

def compare_account(A: dict,B: dict):
    '''
    Takes two accounts and returns who has more followers
    '''
    if A["follower_count"] > B["follower_count"]:
        return "a"
    elif A["follower_count"] < B["follower_count"]:
        return "b"
    else:
        return "c"

def game():
    '''
    The main game logic is executed here
    '''

    score = 0
    continue_game = True

    account1 =pick_account(game_data)

    while continue_game:
        account2 = pick_account(game_data)
        while account1 == account2:
            account2 = pick_account(game_data)

        print(game_logo)
        print(f"Compare A: {account1["name"]}, a {account1["description"]}, from {account1["country"]}")
        print(vs_logo)
        print(f"Compare B: {account2["name"]}, a {account2["description"]}, from {account2["country"]}")

        correct_choice = compare_account(account1,account2) 
        users_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if users_choice == correct_choice:
            score += 1
            account1 = account2
            print("\n" * 20 )
            print(f"You are right! Current score: {score}")
            
        elif correct_choice == "c":
            account1 = account2
            print("\n" * 20 )
            print(f"Both have same no of followers. This one is on us!\nCurrent score: {score}")
            
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False

# Play the game
game()
