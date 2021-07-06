import random # importing random to choose a random secret number

secret_range = range(0, 1001)
secret = random.choice(secret_range) # chooses a random number in that range

guess = 0 # an initialization 
no_of_guesses = 15 # you can change the number of guesses required

print("Guess the number game (The number can vary from 0 to 1000)")

while True:
    inp = input("\nGuess the number : ")
    if inp.isnumeric():
        guess = int(inp)
        no_of_guesses = no_of_guesses - 1
        print("Number of guesses left : ", no_of_guesses)

        if (guess == secret):
            print("Correct guess!\n")
            break
        else:
            if (no_of_guesses <=0):
                print("No more guesses left   T_T")
                break
            elif (secret > guess):
                print("The secret number is greater than your guess")
            else:
                print("The secret number is lesser than your guess")
    else:
        print("Please run the program again and input positive Integer number only\n")
        break