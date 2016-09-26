from mastermind import *

if __name__ == '__main__':

    # the number of pegs in the answer
    size = 4
    # the number of guesses the user gets
    tries = 10
    # the letters allowed representing the colours
    # green, red, blue, yellow, orange, purple
    valid_chars = 'grbyop'

    count = 0
    master_listg = []
    master_listc = []
    # this creates the answer for the game
    answer = create_code(valid_chars, size)
    # user inputs their guess
    guess = input("Please enter your guess of length {X} using"
                  " the letters {Y}:".format(X=size, Y=valid_chars))
    # if count is below 10, user continues to guess and is given clues
    while count < 10:
        while not valid(list(guess), valid_chars, size):
            guess = input("Please enter your guess again of length {X} using"
                          " the letters {Y}:".format(X=size, Y=valid_chars))
        fully_correct = find_fully_correct(answer, list(guess))
        colour_correct = find_colour_correct(answer, list(guess))
        clue = fully_correct + colour_correct
        # store all guesses into a master guess list
        master_listg.append(list(guess))
        # store all clues into a master clue list
        master_listc.append(clue)
        print_game(master_listg, master_listc)
        # if user is correct, programs prints out a you win statement
        if list(guess) == answer:
            print("Congratulations! It took you {N} guess to find the code."
                  .format(N=count))
            break
        guess = ''
        count += 1
    # if count gets to 10, program prints out a you lose statement
    if count == 10:
        print("I'm sorry you lose. The correct code was {ans}."
              .format(ans=answer))
