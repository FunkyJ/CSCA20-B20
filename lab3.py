import doctest

def is_long(sentence):
    '''
    (sentence) -> string
    Given a string, if the length of the string is bigger than 10,
    return 'very long'. Otherwise, return the string 'kinda short'.
    >>> is_long('Apple')
    'kinda short'
    '''
    if len(sentence) > 10:
        return 'very long'
    else:
        return 'kinda short'
    
def longer(sent1,sent2):
    '''
    (word,word) -> string
    Given two strings, returns the length of the longer string.
    >>> longer('potato','apple')
    'potato'
    '''
    if len(sent1) > len(sent2):
        return sent1
    else:
        return sent2

def earlier(word1,word2):
    '''
    (word,word) -> string
    Given two strings made up of lowercase letters, return the string that would
    appear earlier in the dictionary.
    >>> earlier('apple','abby')
    'abby'
    '''
    if word1 < word2:
        return word1
    else:
        return word2

def where(str1,str2):
    '''
    (word,word) -> string
    Given a string and a single-character string, return the index of the first
    occurrence of the second string in the first.
    >>> where('abc','b')
    1
    >>> where('abc','d')
    -1
    '''
    return str1.find(str2)
    
def is_vowel(chara):
    '''
    Given a one-character string, return True if it is a vowel, and return
    False otherwise.
    >>> is_vowel('b')
    False
    >>> is_vowel('a')
    True
    '''
    return chara in 'aeiou'
     

if __name__ == '__main__':
    doctest.testmod(verbose=True)