import doctest

def every_third(L):
    '''
    Given a list L return a new list that contains every third element of the 
    original list, starting at index 0.
    >>> L = [1,2,3,4,5,6,7,8,9,10]
    >>> every_third(L)
    [1, 4, 7, 10]
    '''
    new = []
    for index in range(0,len(L),3):
        new.append(L[index])
    return new

def every_ith(L,i):
    '''
    Given a list L and an integer i as paramaters, return a new list consisting
    of every ith element of L, starting at index 0.
    >>> L = [1,2,3,4,5,6,7,8,9,10]
    >>> every_ith(L,4)
    [1, 5, 9]
    '''
    new = []
    for index in range(0,len(L),i):
        new.append(L[index])
    return new
        
def sum_list(lst):
    '''
    Return the sum of the number in the input list lst
    >>> lst = [1,2,3]
    >>> sum_list(lst)
    6
    '''
    return sum(lst)

def double_list(lst):
    '''
    Take a list of integer lst and double each integer.
    >>> lst = [1,2,3]
    >>> double_list(lst)
    [2, 4, 6]
    '''
    for index in range(len(lst)):
        lst[index] *=2
    return lst

if __name__ == '__main__':
    doctest.testmod(verbose=True)