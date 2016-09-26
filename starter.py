import doctest

def average_list(M):
    '''(list of list of int) -> list of float
    '''
    new = []
    for i in range(len(M)):
        avg = sum(M[i])/len(M[i])
        new.append(avg)
    return new

def increasing(L):
    '''(list of int) -> bool
    '''
    while index in range(len(L)):
        if index < index+1:
            return True
    else:
        return False
        

def merge(L1, L2):
    '''(list of int, list of int) -> (list of int)
    '''
    
    pass

        


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    