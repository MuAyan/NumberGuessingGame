import random

#functions

def selectdifficulty():
    while True:
        try: 
            dif = int(input("Choose a difficulty (1-3): "))
            if dif not in {1, 2, 3}:
                clear()
                print("Please choose an option from 1-3")
            else:
                return dif
        except ValueError:
            clear()
            print("Invalid input, please enter a number.")

def randomNumber(lim):
    return random.randint(1,lim)


def userInput(dif):
    while True:
        try: 
            number = int(input("Choose a number: "))
            if number < 1 or number > 50 * dif:
                clear()
                print(f"Number must be between 1 and {50 * dif}")
            else:
                return number
        except ValueError:
            clear()
            print("Invalid input, please enter a number.")

def clear():
    print("\033[H\033[J", end="")

def start_game():
        gameActive = True
        print("Welcome to my Number Guessing Game")
        dif = selectdifficulty()
        number = randomNumber(50 * dif)
        guessCount = 0
        clear()
        return gameActive, dif, number, guessCount
def evaluate_guess(guess, number, guessCount, dif):
    distance = abs(number - guess)
    gameActive = True
    gameEnd = False
    guessCount += 1
    if guessCount >= 15:
        clear()
        print(f"Sorry, you ran out of guesses. The number was {number}")
        gameEnd = True
    elif distance >= 10:
        print("Number is far away")
        print(f"{15 - guessCount} guesses remaining")
    elif distance < 10 and distance >= 3:
        print("Number is close")
        print(f"{15 - guessCount} guesses remaining")
    elif distance < 3 and distance > 0:
        print("Number is very close")
        print(f"{15 - guessCount} guesses remaining")
    elif distance == 0:
        clear()
        print(f"Good job, you won! You took {guessCount} guesses")
        gameActive, gameEnd = end_screen()
        return guessCount, gameActive, dif, number, gameEnd
    return guessCount, gameActive, dif, number, gameEnd

def end_screen():
    while True:
        playAgain = input("Would you like to play again? (y/n): ")
        clear()   
        gameEnd = False
        gameActive = True
        if playAgain == "y":
            gameEnd = True
            break
        elif playAgain == "n":
            gameActive = False
            break
        else:
            print("Invalid input, Try again.")
    return gameActive, gameEnd



#Game logic
gameActive, dif, number, guessCount = start_game()

while gameActive:
    guess = userInput(dif)
    clear()
    guessCount, gameActive, dif, number, gameEnd = evaluate_guess(guess, number, guessCount, dif)
    if gameEnd:
        gameActive, dif, number, guessCount = start_game()



