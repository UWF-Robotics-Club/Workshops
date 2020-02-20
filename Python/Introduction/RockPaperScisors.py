from random import uniform

abilities = ['Rock', 'Paper', 'Scissors']

print("Welcome to Rock, Paper, Scissors!")
print("You'll be playing against the computer!")
print("Best 2 out of 3 win!")


while 1:
    userWins = 0
    computerWins = 0
    round = 1

    while userWins < 2 and computerWins < 2:
        print("ROUND ", round)
        computerGuess = int(uniform(0, 3))
        j = 0
        for i in abilities:
            j += 1
            print(j, i)
        userGuess = -1
        if userGuess < 1 or userGuess > 3:
            userGuess = int(input("CHOOSE WISELY! \n"))

        userGuess -= 1
        print("The computer chose ", abilities[computerGuess], " and you chose ", abilities[userGuess], "!")

        if (userGuess == 0 and computerGuess == 2) or (userGuess == 1 and computerGuess == 0) or (userGuess == 2 and
                                                                                                  computerGuessGuess == 1):
            print("You've won this round!")
            userWins += 1
        elif userGuess == computerGuess:
            print("This round is a tie! You've got this!")
        else:
            print("The computer won this round! Better luck next time!")
            computerWins += 1
        round += 1
        print()

    if computerWins > userWins:
        print("Looks like the computer is better!")
    else:
        print("You are the champion!")

    if input("Would you like to play again? y or n  ") != 'y':
        break
