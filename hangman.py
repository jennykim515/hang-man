import turtle
import time
import random

wrongGuesses = []
correctGuesses = []
turtle.bgcolor("sky blue")


# clears console
def clear():
    print("\n" * 100)


# gets the secret word from first player
def getSecretWord():
    secret = input("Please enter your secret word: ").lower().strip()
    return secret


# displays board FIRST time to create do-while sort of loop
def displayBoard(secret):
    for char in secret:
        if char == " ":
            print(" ", end="")
        elif char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~", "`", "\"", "'", "|"]:
            print(char, end="")
        else:
            print("_ ", end="")
    print("\n" * 5)


# gets guess from user and makes sure it's a valid input
def getGuess():
    guess = input("What is your guess? ").lower().strip()
    good = False
    while good is False:
        if len(guess) > 1:
            guess = input("Please enter one letter! ")
        elif guess.isdigit():
            guess = input("Please only enter letters! ")
        elif guess in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~", "`", "\"", "'", "|"]:
            guess = input("Please only enter letters! ")
        elif guess == "":
            guess = input("Please enter a letter! ")
        else:
            good = True
    return guess


# compares guess to the secret word and makes sure it's not already guessed before.
def checkGuess(secret, hangManBoard, guess):
    secretList = list(secret)
    # if the guess is not correct
    if guess not in secretList:
        if guess not in wrongGuesses:
            # checks if repeated guess
            # appending to the list of wrong guesses
            wrongGuesses.append(guess)
            return 0
        # returns 1 = nothing gets drawn
        elif guess in wrongGuesses:
            print("You've guessed '" + guess + "' before.")
            return 1

    # if the guess is correct
    else:
        # checks if repeated guess
        if guess in correctGuesses:
            print("You've guessed '" + guess + "' before.")
        else:
            for letter in secretList:
                if letter == guess:
                    x = secretList.index(guess)
                    secretList[x] = x
                    hangManBoard[x] = guess
                    correctGuesses.append(guess)
        print(" ".join(hangManBoard))

        # display letters on graphic
        # turtle.penup()
        # turtle.goto(0, 150)
        # turtle.write(" ".join(hangManBoard), align="center", font=("Arial", 55, "bold"))
        # turtle.hideturtle()
        return 1


# if incorrect guess is made, it draws on turtle
def incorrectGuess(count, guess, window):
    print("There is no '" + guess + "' in the word")

    # head
    if count == 1:
        window.fillcolor('white')
        window.begin_fill()
        window.circle(30)
        window.end_fill()
        window.penup()

    # spine
    if count == 2:
        window.goto(0.00, -60)
        window.pendown()
        window.setheading(270)
        window.forward(100)

    # left leg
    if count == 3:
        window.right(50)
        window.forward(80)
        window.penup()

    # right leg
    if count == 4:
        window.goto(0, -160)
        window.pendown()
        window.left(100)
        window.forward(80)
        window.penup()

    # arm
    if count == 5:
        window.goto(0, -110)
        window.setheading(0)
        window.pendown()
        window.forward(50)
        window.penup()

    # arm 2
    if count == 6:
        window.goto(0, -110)
        window.pendown()
        window.setheading(180)
        window.forward(50)
        window.penup()

    return count


# makes the guessing board
def board(secret):
    secretAsList = list(secret)
    wordAsList = []
    for char in secretAsList:
        if char == " ":
            wordAsList.append(" ")
            correctGuesses.append(" ")
        elif char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~", "`", "\"", "'", "|"]:
            wordAsList.append(char)
            correctGuesses.append(char)
        else:
            wordAsList.append("_")
    return wordAsList


# puts everything together - draws the hanging place
# loops and checks when the game is done
def play(secret, chances):
    window = turtle.Turtle()
    # hanging place
    window.goto(0, 0)
    window.pensize(8)
    window.setheading(90)
    window.pendown()
    window.forward(60)
    window.right(90)

    window.forward(100)
    window.right(90)

    window.forward(300)
    window.penup()

    window.goto(0, -240.00)
    window.left(90)
    window.pendown()
    window.forward(200)
    window.penup()
    window.goto(0.00, 0.00)
    window.setheading(180)
    window.pendown()
    clear()

    hangManBoard = board(secret)
    # count = # of incorrect
    count = 0
    gameOver = False
    displayBoard(secret)
    wordWriter = turtle.Turtle()
    wordWriter.penup()
    wordWriter.hideturtle()
    wordWriter.goto(0, 150)
    wordWriter.write(" ".join(hangManBoard), align="center", font=("Arial", 55, "bold"))
    wordWriter.hideturtle()
    while gameOver is False:
        guess = getGuess()
        incorrect = checkGuess(secret, hangManBoard, guess)
        if incorrect == 1:
            wordWriter.clear()
            wordWriter.goto(0, 150)
            wordWriter.write(" ".join(hangManBoard), align="center", font=("Arial", 55, "bold"))

        elif incorrect == 0:
            count += 1
            tries = incorrectGuess(count, guess, window)
            # of chances you get
            if tries == chances:
                print("Sorry, you lose. The word was '" + secret + "'", end="")
                gameOver = True
                deadMan(secret)

        if len(correctGuesses) == len(secret):
            print("You win! The word was '" + secret + "'", end="")
            aliveMan(secret)
            gameOver = True


# displays "You Lose" when lost
def deadMan(secret):
    time.sleep(1.2)
    turtle.clearscreen()
    turtle.bgcolor("red")
    turtle.hideturtle()
    turtle.write("You Lose! The word was '" + secret + "'", font=("Verdana", 30, "bold"), align="center")


# displays "You Win" when won
def aliveMan(secret):
    time.sleep(1.2)
    turtle.clearscreen()
    turtle.bgcolor("lime")
    turtle.hideturtle()
    turtle.write("You Win!", font=("Verdana", 30, "bold"), align="center")


# play with a computer
def robot(file):
    f = open(file)
    lines = f.readlines()
    secret = (lines[random.randrange(0, len(lines))])
    while len(secret.strip()) <= 3:
        secret = (lines[random.randrange(0, len(lines))])
    return secret.strip().lower()


# Allows user if they want to play with computer or person
def menu():
    choice = input("Would you like to play with computer or another player? c/p: ").lower().strip()
    if choice == "c":
        return 0
    elif choice == "p":
        return 1


def gameMode():
    choice = menu()
    # if wanting to play with computer
    if choice == 0:
        # options
        print("1) animals")
        print("2) food")
        print("3) countries")
        print("4) random words")
        theme = int(input("Please pick a theme: "))
        if theme == 1:
            secret = robot("animals.txt")
            play(secret, chances=6)
        elif theme == 2:
            secret = robot("food.txt")
            play(secret, chances=6)
        elif theme == 3:
            secret = robot("countries.txt")
            play(secret, chances=6)
        elif theme == 4:
            secret = robot("randomWords.txt")
            play(secret, chances=6)
    elif choice == 1:
        chances = input("How many chances? Enter for default: ").strip()
        if chances == "":
            secret = getSecretWord()
            play(secret, chances=6)
        else:
            secret = getSecretWord()
            play(secret, int(chances))


def main():
    print("Let's play Hangman!")
    gameMode()
    repeat = (input("\nWould you like to play again? y to continue: ")).lower().strip()
    while repeat == "y":
        wrongGuesses.clear()
        correctGuesses.clear()
        turtle.clearscreen()
        turtle.bgcolor("sky blue")
        gameMode()
        repeat = (input("\nWould you like to play again? y to continue: ")).lower().strip()
    print("\nThanks for playing!")


main()
