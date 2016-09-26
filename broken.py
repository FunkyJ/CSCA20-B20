"""CSCA20 Lab. Learning to use the debugger."""


def even_len(s):
    """(str) -> bool
    Return whether the length of s is even.
    >>> even_len('')
    True
    >>> even_len('x')
    False
    >>> even_len('abc')
    False
    >>> even_len('abcdef')
    True
    """

    is_even = len(s) % 2 == 0
    return is_even


def every_other(s):
    """(str) -> str
    Return a string that contains every other character from s, in
    order, beginning with the first character.

    >>> every_other('')
    ''
    >>> every_other('x')
    'x'
    >>> every_other('csca20')
    'cc2'
    >>> every_other('csc a20')
    'cca0'
    """

    result = ''
    for i in range(len(s)):
        if (i % 2 == 0):
            result = result + s[i]
    return result


def is_vowel(c):
    """(str) -> bool
    Return whether character c is a vowel.
    >>> is_vowel('a')
    True
    >>> is_vowel('b')
    False
    """

    return c.lower() in 'aeiou'


def stutter(s, k):
    """(str) -> str
    Return a string of characters from s, but with each consonant
    repeated k times.
    >>> stutter('', 24)
    ''
    >>> stutter('aei', 5)
    ''
    >>> stutter('b', 2)
    'bb'
    >>> stutter('acrobat', 3)
    'cccrrrbbbttt'
    """

    result = ''
    for c in s:
        if not is_vowel(c):
            result = result + k * c
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
