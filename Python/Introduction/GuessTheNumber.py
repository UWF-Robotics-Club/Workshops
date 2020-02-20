from random import uniform

playAgain = True

print("Welcome to the Guessing Game!")

while playAgain:

    low = int(input("Please enter the lower range: "))
    high = low-1
    while(high < low):
        high = int(input("Please enter the higher range: "))
        if high < low:
            print("Your upper bound must be larger than the lower bound!")

    toGuess = int(uniform(low+1, high-1))
    print("You'll be guessing for a number between ", low, " and ", high, "!")

    userGuesses = []
    numGuesses = 1

    while 1:

        if numGuesses > 1 :
            if input("Would you like to see your guesses? y or n ") == 'y':
                tempList = userGuesses
                list.sort(tempList)
                print(tempList)

        userGuesses.append(int(input("Make a guess at what the number is: ")))

        if userGuesses[numGuesses-1] != toGuess:
            print("Sorry that's not right! Try again!")
        else:
            print("Congrats! You guessed the right number after ", numGuesses, "tries!")
            break
        if userGuesses[numGuesses-1] > high or userGuesses[numGuesses-1] < low :
            print("Don't forget, your guessing range is between ", low, " and ", high)

        print("You've guessed ", numGuesses, " time(s)!")
        numGuesses += 1
        print()

    if input("Would you like to play again? y or n") != 'y' :
        break
