"""
A general guide for hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""
guesses_left = 10

word_bank = ["batman", "superman", "fast8", "barney", "the flash", "barbie","power rangers", "scary movie", "spider man", "conjuring"]
random_word = word_bank[random.randint(0, len (word_bank)-1)]

letters_guessed = []

current_guess = ''

while guesses_left:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
             output.append(letter)
        else:
             output.append("*")
        print(output)
        guess = input("Guess a letter")






































