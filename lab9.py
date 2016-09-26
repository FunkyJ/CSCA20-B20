import doctest


def open_temperature_file(filename):
    '''(str) -> file
    Open filename, which must be a file, read past its three-line header, and
    return the open file.
    '''
    count = 0
    myfile = open(filename, 'r')
    while count < 3:
        myfile.readline()
        count += 1

    return myfile


def avg_temp_march(f):
    ''' (file) -> float
    Return the average temperature for the month of March for all years
    with data in f.
    >>> avg_temp_march(open_temperature_file('cryer2.dat'))
    32.475
    '''
    march = []
    for line in f:
        march.append(float(line.strip().split('    ')[2]))
    avg_march = sum(march)/len(march)
    return avg_march


def three_highest_temps(f):
    ''' (file) -> list of float
    Return the three highest temperatures, in descending order, for all
    months of all years with data in f.
    >>> three_highest_temps(open_temperature_file('cryer2.dat'))
    [74.0, 73.7, 73.7]
    '''

    mstr_lst = []
    for line in f:
        lst = line.strip().split('    ')
        for i in range(len(lst)):
            mstr_lst.append(float(lst[i]))
    top_three = sorted(mstr_lst, reverse=True)
    return top_three[0:3]


def below_freezing(r):
    ''' (file) -> list of float
    Return the temperatures below freezing (32 degrees Fahrenheit), in
    ascending order, for all months in all years with data in the open file f.
    '''

    FREEZING = 32
    mstr_lst = []
    for line in r:
        lst = line.strip().split('    ')
        for i in range(len(lst)):
            if float(lst[i]) < float(FREEZING):
                mstr_lst.append(float(lst[i]))
    temp_below = sorted(mstr_lst)
    return temp_below


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    filename = 'cryer2.dat'
    # put this in your directory along with this lab file

    # Call the functions and print the results here.
    # for example, this will print all the lines of the file

    reader = open_temperature_file(filename)
    for line in reader:
        print(line, end='')
    reader.close()
