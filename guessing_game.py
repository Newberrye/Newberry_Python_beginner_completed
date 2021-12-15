# if while loops training

# variables to store game rules and player gueses
secret_word = "handy"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# game will loop as long as word isn't guessed and guess limit isn't reached
while secret_word != guess and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guess, YOU LOSE!")
else:
    print("You win!")