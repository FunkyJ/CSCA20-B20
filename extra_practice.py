import doctest

# very basic DNA example:
# DNA strands are a sequence of pairs.  For example
# AcTCgA
# TgAGcT
# where 'A, C, G, T' are the bases and 'A' pairs with 'T' and 'C'
# pairs with 'G'. Case doesn't matter.  Since knowing the bottow half tells
# us the top half, we usually only store the bottom half.

def count_base(dna_sequence, base):
    """(str, str) -> int

    Return the number of times base appears in dna_sequence, in either
    half.

    Parameters:
      dna_sequence : a representation of the DNA sequence
      base : one of 'A', 'a', 'T', 't', 'C', 'c', 'G', 'g'

      >>> count_base('', 'a')            # boundary case: empty
      0
      >>> count_base('T', 't')           # boundary case: singleton
      1
      >>> count_base('gcGCc', 'a')       # typical case: does not appear
      0
      >>> count_base('TcACc', 'c')       # typical case: appears in one half
      3
      >>> count_base('TcACc', 'C')       # typical case: upper case
      3
      >>> count_base('TACgtACGaCGT', 'a')# typical case: appears in both halves
      6

    """

    count = 0
    if base in 'aAtT':
        for gene in dna_sequence:
            if gene in 'aAtT':
                count += 1
    elif base in 'cCgG':
        for gene in dna_sequence:
            if gene in 'cCgG':
                count += 1
    return count


def pairs(dna):
    """(str) -> str

    Return the other half of dna, in all capital letters.

    Parameters:
      dna : a representation of the DNA sequence

    >>> pairs('')              # boundary case: empty
    ''
    >>> pairs('t')             # boundary case: singleton
    'A'
    >>>                        # typical cases: all bases present,
    >>> pairs('TACgtAcGaCGT')  # both upper and lower case
    'ATGCATGCTGCA'
    >>> pairs('aaagtAcGaCGT')
    'TTTCATGCTGCA'
    >>> pairs('TACgtAcGaCGTactg')
    'ATGCATGCTGCATGAC'

    """

    seq = ''
    for gene in dna:
        if gene in 'aA':
            seq += 'T'
        elif gene in 'tT':
            seq += 'A'
        elif gene in 'cC':
            seq += 'G'
        elif gene in 'gG':
            seq += 'C'
    return seq

def common(s1, s2):
    '''(str, str) -> str
    Return a string that is all the characters in the same position
    in both strings.
    >>> common('billy', 'joe')
    ''
    >>> common('aba', 'cbd')
    'b'
    >>> common('banana', 'anna')
    'na'
    >>> common('good morning', 'food poisoning')
    'ood on'
    '''

    new = ''
    length = min(len(s1), len(s2))
    for index in range(length):
        if s1[index] == s2[index]:
            new += s1[index]
    return new
        
            


def count_hydrogen(molecule):
    '''(str) -> int
    Return the number of H atoms in the given molecule.
    >>> count_hydrogen('H20')
    2
    >>> count_hydrogen('NaOH')
    1
    >>> count_hydrogen('He')
    0
    >>> count_hydrogen('CH3OH')
    4
    '''
    # for each letter, go thru molecule
    # check if letter is h
    # if h check next letter if it is integer
    # if integer add to count
    # next letter
    # repeat
    count = 0
    for index in range(len(molecule)):
        if molecule[index] == 'H':
            if index < (len(molecule) - 1):
                if molecule[index+1].isdigit():
                    count += int(molecule[index + 1])
                elif molecule[index +1].islower():
                    continue
                elif molecule[index + 1].isupper():
                    count += 1
            elif index == (len(molecule) - 1):
                count +=1             
    return count


# list functions
def same_types(L):
    '''(list) -> bool
    Return True if all items in L are of the same type and 
    False otherwise.
    >>> same_types([True])
    True
    >>> same_types([])
    True
    >>> same_types([1, 3, 'i'])
    False
    >>> same_types([1, 4, 6, 8])
    True
    '''
    if len(L) < 2:
        return True
    for index in range(len(L)-1):
        if type(L[index]) != type(L[index + 1]):
            return False
    return True


# modify a list

def break_code(L, code):
    '''(list, str) -> NoneType
    Given a list of ints, and a string of characters modify the
    list by converting each int to a character.  Each int is the index 
    for the required character in the code. Each int must be between 0 and 25 inclusive.
    >>> L = [0, 21, 2, 23]
    >>> break_code(L, 'abcdefghijklmnopqrstuvwxyz')
    >>> L
    ['a', 'v', 'c', 'x']
    >>> L = [1, 25, 0]
    >>> break_code(L, 'opqrstuvwxyzabcdefghijklmn')
    >>> L
    ['p', 'n', 'o']
    >>> L = []
    >>> break_code(L, 'abcdefghijklmnopqrstuvwxyz')
    >>> L
    []
    '''
    for index in range(len(L)):
        L[index] = code[L[index]]
        


def grab_names(L):
    '''(list) -> list
    Return a list containing all the fields from L that are names 
    where a name is word that starts with a capital letter.
    >>> grab_names(['Anna', 35, 'lecturer', 'Toronto', 'Canada'])
    ['Anna', 'Toronto', 'Canada']
    >>> grab_names([25, True, 'windy', 'sunny'])
    []
    '''
    lst = []
    for index in range(len(L)):
        if type(L[index]) != type('A'):
            pass
        else:
            if L[index].istitle():
                lst.append(L[index])
    return lst
    

def interleave(list1, list2):
    '''(list, list) -> list
    Return a list that is the contents of list1 and list2 
    interleaved. If one list is longer, add the remainder of the 
    list to the end.
    >>> interleave([1, 4, 7], [2, 5])
    [1, 2, 4, 5, 7]
    >>> interleave([2,3], [])
    [2, 3]
    >>> interleave([], [3, 5, 7])
    [3, 5, 7]
    >>> interleave([1], [2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    '''
    lst = []
    while list1 and list2:
        lst.append(list1.pop(0))
        lst.append(list2.pop(0))
    return lst + list1 + list2




if __name__ == '__main__':
    
    doctest.testmod(verbose= True)