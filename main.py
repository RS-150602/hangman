import os
import random 
from word_list import word_list
from art import stages

print("Welcome to hangman!!!")
rand_word = random.choice(word_list)
word_length = int(len(rand_word))


display = []
for _ in range(word_length):
    display += "_"
lives = 6


while True:
    user_guess = input("Guess the word: ").lower()

    if user_guess in display:
        input("You have already guessed this letter.")

    for position in range(0,word_length):
        letter = rand_word[position]
        if letter == user_guess:
            display[position] = letter
        
    

    if user_guess not in rand_word:
        input(f"you guessed {user_guess}, thats not in the word, you lose a life.")

        lives -= 1
        if lives == 0:
            print("You lose!!!")
            print(f"The word was {rand_word}")
            input("")
            break
        

    if user_guess in display:
      print("You have already chosen this letter.")

    os.system('cls')
    print(stages[lives])
    print(' '.join(display))
    

    if "_" not in display:
        print("You win!!!")
        input("")
        break
