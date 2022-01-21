from art import logo
from art import vs
print(logo)
from game_data import data
from random import randint
import os
data1 = ""
data2 = ""
random_number_history = []
random_number_value = ""
score = 0
clear = lambda: os.system('cls')
def random_number():
    global random_number_value
    global random_number_history
    random_number_value = ""
    random_number_value = randint(0,49)
    if random_number_value in random_number_history:
        random_number()
        return None
    else:
        random_number_history.append(random_number_value)    
def data1_roll():
    global data1
    global random_number_value
    data1 = ""
    random_number()
    data1 = data[random_number_value]   
def data2_roll():
    global data1
    global data2
    global random_number_value
    random_number()
    data2 = data[random_number_value]     
def game():
    global data1
    global data2
    data1_roll()
    print(f'Compare A: {data1["name"]}, {data1["description"]}, {data1["country"]}'.format(data1))
    
    print(vs)
    
    data2_roll()
    print(f'Compare B: {data2["name"]}, {data2["description"]}, {data2["country"]}'.format(data2))
    
def main():
    global data1
    global data2
    global score
    keep_game = True
    game()
    while keep_game:
        guess = input("Who has more follower? Type 'A' or 'B':  ")
        guess.lower()
        if guess.lower() == "a" or guess.lower() == "b":
            if guess.lower() == "a":
                if data1["follower_count"] > data2["follower_count"]:
                    score += 1
                    clear()
                    print(logo)
                    print(f"You're right! Current score: {score}.")
                    game()
                else:
                    keep_game = False
                    clear()
                    print(logo)
                    print(f"Sorry, that's wrong. Final score: {score}")
                    input("Press enter to exit")
            else:
                if data2["follower_count"] > data1["follower_count"]:
                    score += 1
                    clear()
                    print(logo)
                    print(f"You're right! Current score: {score}.")
                    game()
                else:
                    keep_game = False
                    clear()
                    print(logo)
                    print(f"Sorry, that's wrong. Final score: {score}")
                    input("Press enter to exit")
        else:
            print("Invalid choice")
    
        
main()
