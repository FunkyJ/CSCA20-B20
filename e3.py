import doctest


def sum_numbers(s):
    '''
    (str) -> int
    Assume s is a string of non-negative integers seperated by spaces.
    Return the sum of the integers in s.
    45
    >>> sum_numbers('34 3 542 11')
    590
    '''
    new = 0
    current_number = ''
    for index in s:
        if index.isdigit() == True:
            current_number = current_number + index
        if index.isdigit() == False:
            new = int(current_number) + new
            current_number = ''

    return new + int(current_number)


def sum_numbers_list(s):
    '''
    (str) -> int
    Assume s is a string of non-negative integers seperated
    by spaces.  Return the sum of the integers in s.
    >>> sum_numbers_list('45 80 32 3')
    160
    >>> sum_numbers_list('100')
    100
    '''
    return sum((int(i) for i in s.split()))


def int_all(str_list):
    '''
    (list of str) -> list of int
    Return a list of strings from str_list converted to a
    list of ints.
    >>> int_all(['123', '345', '0', '101'])
    [123, 345, 0, 101]
    '''
    for index in range(len(str_list)):
            str_list[index] = int(str_list[index])
    return str_list


def int_all_2(str_list):
    '''
    (list of str) -> NoneType
    Replace every str element of str_list with its corresponding
    int version.
    >>> sl = ['100', '222', '2', '34']
    >>> int_all_2(sl)
    >>> sl
    [100, 222, 2, 34]
    '''
    for index in range(len(str_list)):
        str_list[index] = int(str_list[index])

if __name__ == '__main__':
    doctest.testmod(verbose=True)
