import random

guesses_left = 10

list_word = ["gucci", "polo", "versace", "armani", "obey", "nike", "jordan", "supreme", "stussy", "bape", "addidas"]
random_word = random.choice(list_word)
letters_guessed = []
ranged_word = len(random_word)
print(random_word)
guess = ""
correct = list(random_word)

guess = ""
while guess != "quit":
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))

    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print(letters_guessed)

    if guess not in random_word:
        guesses_left -= 1
        print(guesses_left)
    if output == correct:
        print("You win")
        exit(0)
    if guesses_left == 0:
        print("you loose")
    Guesses = input("Guesses a letter:")
    print("These are your letter %s" % letters_guessed)

    lower = Guesses.lower()
    letters_guessed.append(lower)
