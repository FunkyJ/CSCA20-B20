import doctest


# All functions in this module make these assumptions:
# - The data in the file starts with 3 header lines that are to be ignored.
# - After the header, each line of the file contains the average monthly
#   temperatures for a year (separated by spaces), starting with January.


def open_temperature_file(filename):
    '''(str) -> file

    Open filename, which must be a file, read past its three-line header, and
    return the open file.
    >>> open_temperature_file('temperature.dat')
    <_io.TextIOWrapper name='temperature.dat' mode='r' encoding='cp1252'>
    '''

    count = 0
    myfile = open(filename, 'r')
    while count < 3:
        myfile.readline()
        count += 1

    return myfile


def get_month_list(open_file, mo):
    '''(file, int) -> list

    Return a list of temperatures for the month mo for all years with data
    in open_file, where mo is an integer between 0 and 11, representing January
    to December, respectively. For example for the temperature.dat file,
    January's temperatures would return [24.7, 16,1, 10.4, 21.5, 19.1,
    14.0, 8.4, 11.2, 13.4, 22.5, 17.6, 20.4]
    >>> get_month_list(open_temperature_file('temperature.dat'),0)
    [24.7, 16.1, 10.4, 21.5, 19.1, 14.0, 8.4, 11.2, 13.4, 22.5, 17.6, 20.4]
    >>> get_month_list(open_temperature_file('temperature.dat'),11)
    [20.0, 31.1, 24.6, 26.0, 20.7, 20.4, 23.8, 27.7, 17.3, 20.4, 25.5, 26.2]
    '''

    mstr_lst = []
    for line in open_file:
        lst = line.strip().split('    ')
        mstr_lst.append(float(lst[mo]))
    return mstr_lst


def avg_temp(open_file, mo):
    '''(file, int) -> float

    Return the average temperature for month mo for all years with data
    in open_file, where mo is an integer between 0 and 11, representing
    January to December, respectively.
    >>> avg_temp(open_temperature_file('temperature.dat'),0)
    16.60833333333333
    >>> avg_temp(open_temperature_file('temperature.dat'),5)
    67.49999999999999
    '''
    temp = get_month_list(open_file, mo)
    return sum(temp)/len(temp)


def higher_avg_temp(open_file, mo1, mo2):
    '''(file, int, int) -> int
    Return either mo1 or mo2 (integers representing months in the range 0
    to 11), whichever has the higher average temperature for all years with
    data in open_file. If mo1 and mo2 have the same average
    temperature, then return -1.
    >>> higher_avg_temp(open_temperature_file('temperature.dat'),0,1)
    1
    >>> higher_avg_temp(open_temperature_file('temperature.dat'),5,1)
    5
    >>> higher_avg_temp(open_temperature_file('temperature.dat'),1,1)
    -1
    '''

    mstr_lst = []
    mstr_lst2 = []
    for line in open_file:
        lst = line.strip().split('    ')
        mstr_lst.append(float(lst[mo1]))
        mstr_lst2.append(float(lst[mo2]))
    temp1 = sum(mstr_lst)/len(mstr_lst)
    temp2 = sum(mstr_lst2)/len(mstr_lst2)
    if temp1 > temp2:
        return mo1
    elif temp2 > temp1:
        return mo2
    else:
        return -1


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    filename = 'temperature.dat'
    # put this in your directory along with this lab file

    # Call the functions and print the results here.
    # for example, this will print all the lines of the file

    reader = open_temperature_file(filename)
    for line in reader:
        print(line, end='')
    reader.close()
