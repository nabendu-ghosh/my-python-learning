import random

blackjack_logo = r'''
  ____  _        _    ____ _  __   _     _    ____ _  __
 | __ )| |      / \  / ___| |/ /  | |   / \  / ___| |/ /
 |  _ \| |     / _ \| |   | ' /   | |  / _ \| |   | ' / 
 | |_) | |___ / ___ \ |___| . \ |_| | / ___ \ |___| . \ 
 |____/|_____/_/   \_\____|_|\_\___/ /_/   \_\____|_|\_\

  _______   _______   _______   _______
 |A      | |K      | |Q      | |J      |
 |   ^   | |  _ _  | |  / \  | |   _   |
 |  / \  | | ( v ) | |  \ /  | |  ( )  |
 |  \ /  | |  \ /  | |   v   | |  (_ ) |
 |      A| |      K| |      Q| |      J|
  _______   _______   _______   _______
'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def deal_card(entity,no_of_cards):
    """
    Takes the number of cards needs to be dealt and returns a list
    """
    entity.extend(random.choices(cards, k=no_of_cards))
    return entity

def calculate_score(entity):
    """
    Takes entity/player's cards as input and calculates the score of the current hand
    """
    if sum(entity) > 21 and 11 in entity:
        no_of_aces = entity.count(11)
        score = sum(entity)
        while score > 21 and no_of_aces > 0:
            no_of_aces -= 1
            score -= 10
    else:
        score = sum(entity)
    return score

def decide_winner(entity1, entity2):
    """
    Takes two players cards as input and decides who is the winner. 
    entity1 is player and entity2 is computer.
    """
    if calculate_score(users_cards) == calculate_score(computers_cards):
        print("Draw!")
    elif calculate_score(users_cards) > 21:
        print("You went over. You Lose!")
    elif calculate_score(computers_cards) >21:
        print("Computer Went over. You Win!")
    elif calculate_score(users_cards) > calculate_score(computers_cards):
        print("You scored higher. You Win!")
    else:
        print("You Lose!")

def blackjack_game():
    '''
    Logic for the blackjack game
    '''
    print(blackjack_logo)

    # 1st round of card dealing
    deal_card(users_cards,2)
    deal_card(computers_cards,2)
    print(f"Your cards: {users_cards}, current score: {calculate_score(users_cards)} ")
    print(f"Computer's first card: {computers_cards[0]}")

    # Blackjack check and next rounds
    if calculate_score(users_cards) == 21 and calculate_score(computers_cards) == 21:
        print("Both have Blackjack. Draw!")
    elif calculate_score(users_cards) == 21:
        print("You have Blackjack. You Win!")
    elif calculate_score(computers_cards) == 21:
        print("Computer has Blacjack. Computer Wins!")
    else:
        while calculate_score(computers_cards) < 17:
            deal_card(computers_cards,1)
        while calculate_score(users_cards) < 22:
            draw_another = input("Do you want to draw another card? Type \"y\" or \"n\": ").lower()
            if draw_another == "y":
                deal_card(users_cards,1)
                print(f"Your cards: {users_cards}, current score: {calculate_score(users_cards)} ")
                print(f"Computer's first card: {computers_cards[0]}")
            else:
                break
    #Print final hand and score
    print(f"Your final hand: {users_cards}, final score: {calculate_score(users_cards)} ")
    print(f"Computer's final hand: {computers_cards}, final score: {calculate_score(computers_cards)} ")

    # Decide and announce winner
    decide_winner(users_cards,computers_cards)

while play == "y":
    users_cards = []
    computers_cards = []
    
    blackjack_game()

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        print("\n"* 20)




    

    