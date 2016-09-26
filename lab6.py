import doctest


def longer(s1, s2):
    '''(string,string) -> string
    Given two strings, return the longer string.
    >>> longer('potato','apple')
    'potato'
    >>> longer('','a')
    'a'
    >>> longer('','')
    ''
    >>> longer('adda','adda')
    'adda'
    '''
    if len(s1) > len(s2):
        return s1
    else:
        return s2


def double_list(lst):
    '''(list) -> NoneType
    Takes a list of integers lst and doubles each integers.
    >>> lst = [2,4,6]
    >>> double_list(lst)
    >>> lst
    [4, 8, 12]
    >>> lst = []
    >>> double_list(lst)
    >>> lst
    []
    '''
    for i in range(len(lst)):
        lst[i] *= 2


def circle_area(r):
    '''(float) -> float
    Return the area of a circle of radius r.
    >>> circle_area(2)
    12.56
    >>> circle_area(0)
    0.0
    '''
    return 3.14 * (r ** 2)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
