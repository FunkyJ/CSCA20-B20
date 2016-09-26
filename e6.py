"""Exercise 6, CSCA20."""
import doctest


def strs_to_dict(coded, plain):
    """(str, str) -> dict of {str: str}

    Return a dict in which the keys are the characters in coded and
    the values are the characters in the same positions in plain. The
    two parameters must have the same length.

    >>> d = strs_to_dict('etaoin', 'shrdlu')
    >>> d == {'e': 's', 't': 'h', 'a': 'r', 'o': 'd', 'i': 'l', 'n': 'u'}
    True
    """
    s_d = dict(zip(list(coded), list(plain)))
    return s_d


def decode(s, decoder):
    """(str, dict of {str: str}) -> str

    Return a decoded version of s using the decoder. I.e., return a
    string which is constructed by replacing every character in s with
    the value of this character in decoder.

    >>> d = {'e': 's', 't': 'h', 'a': 'r', 'o': 'd', 'i': 'l', 'n': 'u'}
    >>> decode('inet', d)
    'lush'
    """
    result = ''
    for key in s:
        cipher = decoder.get(key)
        result += cipher
    return result


def type_subdicts(d):
    """(dict) -> dict of {type: dict}

    Return a new dictionary with keys that are types; the value
    corresponding to the key that is the int type is a dictionary
    containing just the key-value pairs from d where the keys are
    ints, and similarly for the types float and str. It is assumed
    that all keys in d are of type int, float or str.

    If there are no keys of type int in d, the corresponding dict in
    the return value is empty, and similarly for types float and str.

    >>> new_d = type_subdicts({1: 'hi', 3.0: '5', 'hi': 5, 'hello': 10})
    >>> new_d[int]
    {1: 'hi'}
    >>> new_d[float]
    {3.0: '5'}
    >>> new_d[str] == {'hi': 5, 'hello': 10}
    True
    """
    subdict = {}
    subdict[int] = {}
    subdict[float] = {}
    subdict[str] = {}
    for key, value in d.items():
        if isinstance(key, int):
            subdict[int][key] = value
        if isinstance(key, float):
            subdict[float][key] = value
        if isinstance(key, str):
            subdict[str][key] = value
    return subdict


if __name__ == '__main__':
    doctest.testmod()
