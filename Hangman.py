import random

def hangman():
    
    gallows = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

    word_list = ["aardvark", "baboon", "camel"]
    word = word_list[random.randrange(0, len(word_list))]
    #could have used random.choice(word_list) instead

    guess_list = []
    for letter in word:
        guess_list.append(letter)

    lives = 6
    display = []

    for x in range(0, len(guess_list)):
        display.append("_")

    while lives > 0:
        guess = ""
        while len(guess) == 0 or len(guess) > 1:
            guess = input("Guess a letter in the word: ")
            if len(guess) > 1:
                print("Please enter only one letter.")
            guess = guess.lower()
        print(f"You guessed: {guess}")

        if guess in display:
            print("you have already guessed this.")

        for i in range(0, len(guess_list)):
            if guess == guess_list[i]:
                display[i] = guess
                
        if guess not in guess_list:
            lives -= 1
            print(f"you have {lives} lives left.")
        
        print(*display)
        print(gallows[lives])

        if "_" not in display:
            print("you win")
            break

    if lives == 0:
        print("you lose. game over.")
        
