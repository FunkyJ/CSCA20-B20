import doctest
import random


def create_code(s1, num):
    '''(str,int) -> list
    Given a str and a size(int) return a list of length size of single
    character str comprised of the characters in the given str.
    '''
    answer = []
    for i in range(num):
        answer.append(random.choice(s1))
    return answer


def valid(guess, valid_chars, size):
    ''' (list, str, int) -> boolean
    Given a list of single character str, a str and a int that is the length
    of the guess, return True if every character is in the given str and the
    guess is the correct length.
    >>> valid(['g','g','g','g'], 'gbyrop', 4)
    True
    >>> valid(['p','e','z','y'], 'gbyrop', 4)
    False
    >>> valid(['g','g','g','g','g'], 'gbyrop', 4)
    False
    '''
    if len(guess) != size:
        return False
    for letter in guess:
        if letter not in valid_chars:
            return False
    return True


def find_fully_correct(answer, guess):
    '''(list, list) - > list
    Return a list containing a 'b' for each correctly positioned colour
    in the list guess.
    >>> find_fully_correct(['p','o','o','r'], ['g','n','o','r'])
    ['b', 'b']
    >>> find_fully_correct(['p','o','o','r'], ['p','b','b','b'])
    ['b']
    >>> find_fully_correct(['p','r','o','g'], ['g','g','g','r'])
    []
    '''
    b_clue = []
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            b_clue.append('b')
    return b_clue


def remove_fully_correct(list1, list2):
    '''(list, list) -> list
    Return a list that is the result of removing from list1 items that are the
    same and in the same position in list2.
    >>> remove_fully_correct(['y','n','g','g'], ['g','n','g','g'])
    ['y']
    >>> remove_fully_correct(['y','n','r','o'], ['y','n','o','r'])
    ['r', 'o']
    >>> remove_fully_correct(['g','n','o','r'], ['g','n','o','r'])
    []
    '''
    removed = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            removed.append(list1[i])
    return removed


def find_colour_correct(answer, guess):
    '''(list, list) -> list
    Return a list containing a 'w' for each correct colour in the list guess
    that is not in the same position.
    >>> find_colour_correct(['y','n','r','o'], ['y','n','o','r'])
    ['w', 'w']
    >>> find_colour_correct(['b','r','r','g'], ['b','o','r','r'])
    ['w']
    >>> find_colour_correct(['p','b','r','g'], ['y','y','o','y'])
    []
    '''
    w_clue = []
    # create comparison for colours that are the same but not in same position
    compare1 = remove_fully_correct(answer, guess)
    compare2 = remove_fully_correct(guess, answer)
    for i in range(len(compare2)):
        if compare2[i] in compare1:
            compare1.remove(compare2[i])
            w_clue.append('w')
    return w_clue


def print_game(guess, clue):
    ''' list, list) -> NoneType
    Given two list of lists, print to the display each guess separated by
    a tab and the clues that relate.
    '''
    print('Guesses' + ' \t ' + 'Clues')
    for i in range(len(guess)):
        print(' '.join(guess[i]) + ' \t ' + ' '.join(clue[i]))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
