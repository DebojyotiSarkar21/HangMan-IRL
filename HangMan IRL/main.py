import random


from Hangman_words import word_list

chosen_word = random.choice(word_list)

from Hangman_art import logo, stages
print(logo)


lives = 6
display = []

display += chosen_word[0] + chosen_word[1]
for _ in range(len(chosen_word) - 1):
    display += "_"
print(display)



end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:\n").lower()



    if guess in display:
        print(f"You've already guessed {guess}")


    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 1:
            print("LAST CHANCE\nTO\nSAVE THE MAN")
        if lives == 0:
            end_of_game = True
            print(" YOU LOSE. ")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(" YOU WIN. ")



    print(stages[lives])