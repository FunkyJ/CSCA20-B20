import doctest


def count_letter(s1, s2):
    '''
    Given a string s1 and a single-character string s2, returns all the number
    of occurences of the second string in the first.
    >>> count_letter('banana', 'a')
    3
    '''
    count = 0
    for letter in s1:
        if letter == s2:
            count = count + 1
    return count


def remove_digits(s):
    '''
    Given a string s, return the same string without digits.
    >>> remove_digits('123abc')
    'abc'
    '''
    new = ''
    for digit in s:
        if not digit.isdigit():
            digit.replace(digit, '')
            new = new + digit
    return new


def repeat_character(s1, s2):
    '''
    Given a string s1 and a single-character string s2, return a string
    consisting of the single-character string repeated as many times it occurs
    in the first string.
    >>> repeat_character('banana', 'a')
    'aaa'
    '''
    return count_letter(s1, s2) * s2


def every_other(s):
    '''
    Given a string s, return a string built from all characters of s at
    even indices.
    >>> every_other('apple')
    'ape'
    '''
    new = ''
    for index in range(len(s)):
        if (index % 2 == 0):
            new = new + s[index]
    return new

if __name__ == '__main__':
    doctest.testmod(verbose=True)
