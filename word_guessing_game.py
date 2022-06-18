import random;

import nltk;

nltk.download('words');

from nltk.corpus import words;

words = words.words();
def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character. ")
        else:
            return guess
def update_dashes(word,dashes,guess):
    for i in range(len(word)):
        if word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i + 1:]
    return dashes
secret_word = random.choice(words)
dashes = "-" * len(secret_word)
guesses_left = 20
while guesses_left > 0 and dashes != secret_word:
    print(dashes)
    print(str(guesses_left) + " Incorrect guesses left")
    guess = get_guess()
    dashes = update_dashes(secret_word,dashes,guess)
    if guess in secret_word:
        print("the letter is in the secret word")
    else:
        print("the letter is not in the secret word")
        guesses_left = guesses_left - 1

if guesses_left == 0:
    print("You lose. The word was: " + secret_word)
else:
    print("Congrats! You win. The word was:  " + secret_word)
