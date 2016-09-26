"""CSCA20 Lab 10."""


def dict_to_str(d):
    """(dict) -> str
    Return a string containing each key and value in d. Keys and
    values are separated by a space. Each key-value pair is separated
    by a comma.
    """

    d_s = ''.join('{} {},'.format(key, value) for key, value in d.items())
    return d_s


def dict_to_str_sorted(d):
    """(dict) -> str
    Return a string containing each key and value in d. Keys and
    values are separated by a space. Each key-value pair is separated
    by a comma, and the pairs are sorted in ascending order by key.
    """

    d_s = ''.join('{} {},'.format(key, value) for key, value in
                  sorted(d.items()))
    return d_s


def file_to_dict(f):
    """(reader) -> dict of {float: int}
    Given an open file f that contains exchange rate changes, return a
    dict of how many times each rate change occurred, with rate
    changes as keys and the number of occurrences of the changes as
    values. f contains floating point numbers separated by whitespace.
    """
    lst = {}
    for rate in f:
        for i in rate.split():
            lst[float(i)] = lst.get(float(i), 0) + 1
    return lst


def count_changes(d):
    """(dict of {float: int}) -> int
    Assuming d contains keys that are exchange rate changes and values
    that are the number of occurrences of each exchange rate change,
    return the total number of exchange rate changes (including
    duplicates).
    """

    return (sum(d.values()))


def most_common_rate_changes(d):
    """(dict of {float: int}) -> list of float
    Assuming d contains keys that are exchange rate changes and values
    that are the number of occurrences of each exchange rate change,
    return a list of the exchange rate changes, sorted by frequency of
    occurrence from most frequent to least frequent.
    """
    lst = []
    mstr_lst = []
    for key, value in d.items():
        lst.append([value, key])
        result = sorted(lst, reverse=True)
    for i in result:
        mstr_lst.append(float(i[1]))
    return mstr_lst


if __name__ == '__main__':
    testfile = 'exchange-rates-testing.txt'
    fullfile = 'exchange-rates.txt'
    reader = open(testfile, 'r')
    for line in reader:
        print(line, end='')
    reader.close()
