import random
import HangmanWords
import HangmanArt


def hangman():
    print("Welcome to...")
    print(HangmanArt.title)

    lives = 6
    display = []
    guesses = []
    word_list = HangmanWords.word_list
    word = word_list[random.randrange(0, len(word_list))]  # could have used random.choice(word_list) instead

    # parse chosen word into a list of characters
    guess_list = []
    for letter in word:
        guess_list.append(letter)

    # fill display list with blanks the same length as the chosen word
    for characters in range(0, len(guess_list)):
        display.append("_")

    # run while loop for letter guesses until the users lives reach 0
    while lives > 0:
        guess = ""  # initialize guess string
        while len(guess) == 0 or len(guess) > 1 or guess.isalpha() is False:  # data validation
            guess = input("Guess a letter in the word: ")  # user input

            if len(guess) > 1:  # data validation for multiple characters
                print("Please enter only one letter.")
            if guess.isalpha() is False:  # data validation for non-letter characters
                print("Please enter only letters.")

            guess = guess.lower()  # cast guess to lower case for comparison to word bank

        if guess not in guess_list and guess not in guesses:  # discover incorrect guesses
            lives -= 1
            print("your guess was incorrect.")
        elif guess in guess_list and guess in guesses:  # remind user of double guesses
            print("you have already guessed this correctly.")
        elif guess in guesses:  # prevent incorrect double guesses from causing a penalty
            print("you have already guessed this incorrectly.")

        if guess not in guesses:
            guesses.append(guess)  # add guess to list of letters guessed

        print("you have guessed the letters: ", end="")  # display previous guesses for the user
        print(*guesses)

        for i in range(0, len(guess_list)):  # replace chosen word blanks with correct guess
            if guess == guess_list[i]:
                display[i] = guess

        print(*display)  # print current guess state without any commas, quotations, or square brackets
        print(HangmanArt.gallows[lives])  # display gallows stage based on number of lives
        print(f"you have {lives} lives left.")  # display number of lives left

        if "_" not in display:  # if there are no blanks left to fill, user wins
            print("you win")
            break

    if lives == 0:  # if lives fall to zero, user loses
        print("you lose. game over.")
        print(f"your word was {word}")
