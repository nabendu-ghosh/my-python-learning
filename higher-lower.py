import random
from higher_lower_data import game_data, game_logo, vs_logo

score = 0
lives = 1
def pick_account(accounts_list: list):
    return random.choice(accounts_list)

def compare_account(A: dict,B: dict):
    if A["follower_count"] > B["follower_count"]:
        return "a"
    elif A["follower_count"] < B["follower_count"]:
        return "b"
    else:
        return "c"


account1 = pick_account(game_data)
while lives != 0:
    new_list = game_data
    new_list.remove(account1)
    account2 = pick_account(new_list)

    print(f"Compare A: {account1["name"]}, a {account1["description"]}, from {account1["country"]}, followers: {account1["follower_count"]}.")
    print(f"Compare B: {account2["name"]}, a {account2["description"]}, from {account2["country"]}, followers: {account2["follower_count"]}.")

    correct_choice = compare_account(account1,account2) 
    users_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if users_choice == correct_choice:
        score += 1
        account1 = account2
        print(f"You are right! Current score: {score}")
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        lives = 0


