import random as r
from hangman_art import stages
from hangman_art import logo
print(logo)
print("Welcome to hangman! I kept a random game name in my program. Just try to find it!")
from hangman_words import word_list
choosen_word = r.choice(word_list)



#Create Blanks
display = []
word_lenght = len(choosen_word)
for _ in range (word_lenght):
    display += "_"

end = False
health = 6

while not end:

    #Take guess
    guess = input("Tell me a letter!: ").lower()
    
    #Write the correct letter

    for position in range (word_lenght):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
                     
    
    if guess not in choosen_word:
        health -= 1
        if health == 0:
            print("You lose!!!")
            end = True


            
    
    print(f"{' '.join(display)}")
    print(stages[health])
    if "_" not in display:
        print("You win!")
        end = True
                
            
