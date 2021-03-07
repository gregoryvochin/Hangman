#Step 1 

#TODO-1 - Randomly choose a word from the word_list and
#         assign it to a variable called chosen_word.
import random

word = word_list[random.randrange(0, len(word_list))]
#could have used random.choice(word_list) instead
print(word)

word_list = []
for letter in word:
    word_list.append(letter)
    print(word_list)

#TODO-2 - Ask the user to guess a letter and assign their
#         answer to a variable called guess. Make guess lowercase.
guess = ""
while len(guess) == 0 or len(guess) > 1:
    guess = input("Guess a letter in the word: ")
    if len(guess) > 1:
        print("Please enter only one letter.")
    guess = guess.lower()
print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is
#         one of the letters in the chosen_word.

if guess in word_list:
    print("you guessed a letter correctly")

else:
    print("lol scrub")
