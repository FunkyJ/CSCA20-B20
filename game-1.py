from mastermind import *

if __name__ == '__main__':

    # the number of pegs in the answer
    size = 4
    # the number of guesses the user gets
    tries = 10
    # the letters allowed representing the colours
    # green, red, blue, yellow, orange, purple
    valid_chars = 'grbyop'

    # fill in the rest...
    while True:
        count = 0
        master_listg = []
        master_listc = []
        answer = create_code(valid_chars, size)
        guess = input('Please enter your guess of length {X} using the letters {Y}:'.format(X=size, Y=valid_chars))

        while count < 10:
            while not valid(guess, valid_chars, size):
                guess = input('Please enter your guess again of length {X} using the letters {Y}:'.format(X=size, Y=valid_chars))
            fully_correct = find_fully_correct(answer, list(guess))
            colour_correct = find_colour_correct(answer, list(guess))
            clue = fully_correct + colour_correct
            master_listg.append(list(guess))
            master_listc.append(clue)
            print_game(master_listg, master_listc)
            if list(guess) == answer:
                print("Congratulations! It took you {N} guesses to find the code.".format(N=count))
                break        
            guess = ''
            count += 1

        if count == 10:
            print("I'm sorry you lose. The correct code was {Z}.".format(Z=answer))
        rs = input('Restart? (y/n):')
        while rs not in ['y','n']:
            print('Invalid Input')
            rs = input('Restart? (y/n):')
        if rs == 'y':
            continue
        else:
            print('Bye Bye.')
            break
