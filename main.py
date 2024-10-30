#python list
import random
from hangman_words import word_list
from hangman_art import stages,logo

lives = 6
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over =False
corrected_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in corrected_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            corrected_letters.append(letter)
        elif letter in corrected_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: "+ display)



    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} that is not in the word. you lose a life")
        if lives == 0:
            game_over =True
            print(f"******************************************* IT WAS {chosen_word}! You lose *******************************************. ")

    if "_" not in display:
        game_over =True
        print("******************************************* You Win *******************************************")

    print(stages[lives])