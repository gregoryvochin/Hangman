import random
import HangmanWords
import HangmanArt

def hangman():

    lives = 6
    display = []
    guesses = []
    word_list = HangmanWords.word_list
    word = word_list[random.randrange(0, len(word_list))]  #could have used random.choice(word_list) instead

    #parse chosen word into a list of characters
    guess_list = []
    for letter in word:
        guess_list.append(letter)

    #fill display list with blanks the same length as the chosen word
    for characters in range(0, len(guess_list)):
        display.append("_")

    #run while loop for letter guesses until the users lives reach 0
    while lives > 0:
        guess = ""  #initialize guess string
        while len(guess) == 0 or len(guess) > 1 or guess.isalpha() == False:  #data validation
            guess = input("Guess a letter in the word: ")  #user input

            if len(guess) > 1:  #data validatoin for multiple characters
                print("Please enter only one letter.")
            if guess.isalpha() == False:  #data validation for non-letter characters
                print("Please enter only letters.")
                
            guess = guess.lower()
            if guess in guesses:
                print("you have already guessed this.")
            guesses.append(guess)
        print(f"You guessed: {guess}")

        for i in range(0, len(guess_list)):
            if guess == guess_list[i]:
                display[i] = guess
                
        if guess not in guess_list:
            lives -= 1
            print("your guess was incorrect.")
            print(f"you have {lives} lives left.")
        
        print(*display)
        print(HangmanArt.gallows[lives])

        if "_" not in display:
            print("you win")
            break

    if lives == 0:
        print("you lose. game over.")
        print(f"your word was {word}")
        
