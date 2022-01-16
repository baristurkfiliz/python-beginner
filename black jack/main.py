from art import logo
print(logo)
from values import cards
import random
import re

card_history = []
total_score = 0
dealer_score = 0
dealer_wants_card = True
random_card = ""
value = 0

def random_card_s():
    global random_card
    global value
    for i in range(random.randint(0,9)):
        random_card = ""
        value = 0
        random_card = cards.popitem()
        value = random_card[1]
def beginning():
    global total_score
    global dealer_score
    global random_card
    global value
    random_card_s()
    total_score += value
    print(f"You got {random_card[0]}. Your score is {total_score}.")
    random_card_s()
    total_score += value
    print(f"You got {random_card[0]}. Your score is {total_score}.")
    random_card_s()
    dealer_score += value
    print(f"Dealer got {random_card}. Dealer score is {dealer_score}.")
    main()
def dealer_turn():
    global dealer_score
    global dealer_wants_card
    global random_card
    global value
    print("Dealer Turn!")
    if dealer_score >= 17:
        dealer_wants_card = False
        end_game()
    elif dealer_score == 21:
        print("Dealer has 21. It's Blackjack and you lose!")
        exit()
    while dealer_wants_card:
        random_card_s()
        dealer_score += value
        print(f"Dealer got {random_card[0]}. Dealer score is {dealer_score}.")
        return dealer_turn()
def draw_card():
    global total_score
    global random_card
    global value
    in_game = True
    while in_game:
        random_card_s()
        if value == 1:
            Ace_choice = True
            while Ace_choice:
                Ace = input("You got Ace. Do you want 1 or 11?")
                if Ace == "11":
                    total_score += 11
                    main()
                elif Ace == "1":
                    total_score += 1
                    main()
                else:
                    print("Invalid choice.")
                    continue
        else:
            print(f"You got a {random_card[0]}.")
            total_score += value
            main()
def main():
    global dealer_wants_card
    global total_score
    if total_score >= 22:
        print(f"Your score is {total_score}.You lose!")
        exit()
    elif total_score == 21:
        print("You win!")
        exit()
    else:
        Gamer_choice = True
        while Gamer_choice:
            want_to_draw = input(f"Your score is {total_score}. Do you want to draw a card? y or n:  ")
            if want_to_draw == "n":
                if dealer_wants_card == True:
                    dealer_turn()
                else:
                    print(f"Your score is {total_score}. Dealer score is {dealer_score}.")
                    if dealer_score >= total_score:
                        print("Dealer win!")
                        exit()
                    else:
                        print("You win!")   
                        exit()          
            elif want_to_draw == "y":
                draw_card()
            else:
                print("Invalid choice.")
def end_game():
    print(f"Your score is {total_score}. Dealer score is {dealer_score}.")
    if dealer_score >= total_score:
        print("Dealer win!")
        exit()
    else:
        print("You win!")   
        exit()

beginning()