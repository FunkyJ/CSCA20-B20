import  sqlite3


def run_query(db, query, args=None):
    '''(str, str, [tuple]) -> list of tuple
    Return the results of running the given query on database db.'''

    con =  sqlite3.connect(db)
    cur =  con.cursor()
    if args == None:
        cur.execute(query)
    else:
        cur.execute(query, args)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data


def run_command(db, command, args=None):
    '''(str, str, [tuple]) -> NoneType
    Execute the given command with the args on database db.'''

    con =  sqlite3.connect(db)
    cur =  con.cursor()
    if args == None:
        cur.execute(command)
    else:
        cur.execute(command, args)
    cur.close()
    con.commit()
    con.close()


def setup_accounts(db, filename):
    '''(str, str) -> NoneType
    Create and populate the Accounts table for database db using the
    contents of the file named filename.'''
    # open file
    data_file = open(filename)
    # connect to database
    con =  sqlite3.connect(db)
    # create cursor
    cur = con.cursor()

    # create and populate the table here
    cur.execute('''CREATE TABLE Accounts(Number TEXT, Savings REAL,
    Chequing REAL)''')
    # insert values into Accounts table
    for line in data_file:
        data = line.split(',')
        cur.execute('INSERT INTO Accounts VALUES(?,?,?)',
                    (data[0].strip(), float(data[1].strip()),
                     float(data[2].strip())))
    # close file
    data_file.close()
    # close cursor
    cur.close()
    # commit changes
    con.commit()
    # close connection
    con.close()


def setup_transactions(db, filename):
    '''(str, str) -> NoneType
    Create and populate the Transactions table for database db using the
    contents of the file named filename.'''
    # open file
    data_file = open(filename)
    # connect to database
    con =  sqlite3.connect(db)
    # create cursor
    cur = con.cursor()

    # create and populate the table here
    cur.execute('''CREATE TABLE Transactions(Date TEXT, Number TEXT, Type TEXT,
    PayFrom TEXT, PayTo TEXT, Amount REAL)''')
    # insert values into Transactions table
    for line in data_file:
        data = line.split(',')
        cur.execute('''INSERT INTO Transactions VALUES(?,?,?,?,?,?)''',
                    (data[0].strip(), data[1].strip(), data[2].strip(),
                     data[3].strip(), data[4].strip(),
                     float(data[5].strip())))

    # close file
    data_file.close()
    # close cursor
    cur.close()
    # commit changes
    con.commit()
    # close connection
    con.close()


def setup_security(db, filename):
    '''(str, str) -> NoneType
    Create and populate the Security table for database db using the
    contents of the file named filename.'''
    # open file
    data_file = open(filename)
    # connect to database
    con = sqlite3.connect(db)
    # create cursor
    cur = con.cursor()

    # create and populate the table here
    cur.execute('''CREATE TABLE Security(Number TEXT, Password TEXT, Name TEXT,
    Address TEXT)''')
    # insert values into Security table
    for line in data_file:
        data = line.split(',')
        cur.execute('''INSERT INTO Security VALUES(?,?,?,?)''',
                    (data[0].strip(), data[1].strip(), data[2].strip(),
                     data[3].strip()))

    # close file
    data_file.close()
    # close cursor
    cur.close()
    # commit changes
    con.commit()
    # close connection
    con.close()


def get_account_balances(dbname, number):
    '''(str, str) -> list of 2-tuple
    Given a database name and the client number, return the savings
    and chequing balances.
    '''
    # select Savings and Chequing balance from the Account table with the
    # account number provided
    return run_query(dbname, 'SELECT Savings, Chequing FROM Accounts WHERE' +
                     ' number = (?)', (number,))


def get_transactions(dbname, number, from_account, to_account):
    '''(str, str, str, str) -> list of 2-tuples
    Return all transaction from the bank account number ordered by the date
    , where the transaction is the money moved from the account from_account
    to the account to_account.
    '''
    # select Date and Amount from the Transactions table with the account
    # number provided
    return run_query(dbname, 'SELECT Date, Amount FROM Transactions WHERE' +
                     ' Number = (?) And PayFrom = (?) AND PayTo = (?)',
                     (number, from_account, to_account))


def get_bills(dbname, number, from_account):
    '''(str, str, str) -> list of tuples
    Return a list of tuples of the bills paid from from_account.
    '''
    # select only the unique account number's payments from the Transactions
    # table with the account number provided
    return run_query(dbname, 'SELECT DISTINCT PayTo FROM Transactions' +
                     ' WHERE Number = (?) AND PayFrom = (?)',
                     (number, from_account))


def get_account_info(dbname, number):
    ''' (str, str) -> list of single tuple
    Return the client's name, address, savings and chequing account balances
    based on the client number provided.
    '''
    # select the Name, Address, Savings, and Chequing from a joined table
    # between the Security and Accounts table based on the account number
    # provided
    return run_query(dbname, 'SELECT Security.Name, Security.Address,' +
                     ' Accounts.Savings, Accounts.Chequing FROM Security' +
                     ' JOIN Accounts WHERE Security.Number == (?) AND ' +
                     'Accounts.Number == (?)', (number, number))


def update_account_balance(dbname, number, account, balance_change):
    ''' (str, str, str, float) -> float
    Return an updated account balance for the bank number in the type of
    account (savings/chequing) by changing the present balance.
    '''
    # find out which account is being balanced
    # update the account from the Accounts table based on the account number
    # provided
    # create a variable that grabs the current balance
    # then add it to a new variable to obtain the final balance
    if account == 'Savings':
        balance = run_query(dbname, 'SELECT Savings FROM Accounts WHERE' +
                            ' number = (?)', (number,))
        new_balance = float(balance[0][0]) + float(balance_change)
        run_command(dbname, 'UPDATE Accounts SET Savings = (?)' +
                    ' WHERE number = (?)', (new_balance, number))
    else:
        balance = run_query(dbname, 'SELECT Chequing FROM Accounts WHERE' +
                            ' number = (?)', (number,))
        new_balance = float(balance[0][0]) + float(balance_change)
        run_command(dbname, 'UPDATE Accounts SET Chequing = (?)' +
                    ' WHERE number = (?)', (new_balance, number))
    return new_balance


def pay_bill(dbname, bill, number, account, amount, date):
    ''' (str, str, str, str, float, str) -> float
    Update the balance of the given account to reflect the bill payment in the
    database, insert the bill payment as a transcation in the database, and
    then return the new balance.
    '''
    # create the bill payment which will be 0 - float(amount)
    # because we have created an update balance function already, we can
    # re-use the function
    new_balance = update_account_balance(dbname, number, account, 0 -
                                         float(amount))
    # insert the new line in the Transaction table of the bill payment
    run_command(dbname, 'INSERT INTO Transactions VALUES(?, ?, ?, ?, ?, ?)',
                (date, number, 'Bill', account, bill, amount))
    return new_balance


def sum_transactions(dbname, number, date):
    ''' (str, str, str) -> list of tuples
    Return the name of the bill and the total amount paid after a given date
    based on the client number.
    '''
    # create the total transaction of one bill by selecting the PayTo and the
    # sum of the amounts from the Transactions table based on the account
    # number and the type
    # group the total transactions based on PayTo
    total = run_query(dbname, "SELECT PayTo, SUM(Amount) FROM Transactions" +
                      " WHERE Number = (?) AND Date > (?) AND Type = 'Bill'" +
                      " GROUP BY PayTo", (number, date))
    return total


def transfer_funds(dbname, number, from_account, to_account, amount, date):
    '''(str, str, str, float, str) -> list of float
    Add a row to the transactions table, update the account balance and
    return the new account balances as a list where the the first item
    is the new balance for the "from" account and the second item is the
    new balance of the "to" account.
    '''

    from_new_balance = update_account_balance(dbname, number, from_account,
                                              (0-amount))
    to_new_balance = update_account_balance(dbname, number, to_account, amount)
    run_command(dbname, '''INSERT INTO Transactions VALUES(?,?,?,?,?,?)''',
                (date, number, 'Transfer', from_account, to_account, amount))

    return [from_new_balance, to_new_balance]
