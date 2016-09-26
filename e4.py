import doctest


def average_list(M):
    '''(list of list of int) -> list of float
    Return a list of floats where each float is the average of the
    corresponding list in the given list of lists.
    >>> M = [[0,2,1],[4,4],[10,20,40,50]]
    >>> average_list(M)
    [1.0, 4.0, 30.0]
    >>> M = []
    >>> average_list(M)
    []
    '''
    new = []
    for i in range(len(M)):
        avg = sum(M[i])/len(M[i])
        new.append(avg)
    return new


def increasing(L):
    '''(list of int) -> bool
    Return True if the given list of ints is in increasing order and
    False otherwise.
    >>> increasing([4,3,2,1])
    False
    >>> increasing([2,4,6,8])
    True
    >>> increasing([0,0,1,2])
    False
    >>> increasing([3])
    True
    >>> increasing([1,2,4,3])
    False
    '''
    index = 0
    while index < (len(L)-1):
        if L[index] >= L[index+1]:
            return False
        index += 1
    return True


def merge(L1, L2):
    '''(list of int, list of int) -> (list of int)
    Return a list of ints sorted in increasing order that is the merge
    of the given sorted lists of integers.
    >>> merge([0,2,4],[1,3,5])
    [0, 1, 2, 3, 4, 5]
    >>> merge([2,4],[1,2,4])
    [1, 2, 2, 4, 4]
    >>> merge([0,1,2],[3,4])
    [0, 1, 2, 3, 4]
    >>> merge([],[1,3,4])
    [1, 3, 4]
    '''
    new_lst = []
    while L1 and L2:
        if L1[0] < L2[0]:
            new_lst.append(L1.pop(0))
        elif L1[0] > L2[0]:
            new_lst.append(L2.pop(0))
        else:
            new_lst.append(L1.pop(0))
            new_lst.append(L2.pop(0))
    return new_lst + L1 + L2


if __name__ == '__main__':
    doctest.testmod(verbose=True)
