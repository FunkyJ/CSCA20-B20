import sqlite3
from datetime import datetime

def create_customers(db, data_file):
    '''Create and populate the Customer table with
    the data from the open file data_file.'''
    
    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor
    cur = con.cursor()
    
    # Create the customer table
    cur.execute('''CREATE TABLE Customers(id TEXT,last_name TEXT,first_name 
    TEXT,street_num TEXT,street_name TEXT,city TEXT,province TEXT,code TEXT,
    tel TEXT,alt_tel TEXT,email TEXT)''')

    # Populate the Custormer Table
    # Loop through each line in the file:
    for line in data_file:
        # Split the data in each line and store in a 
        # list called data
        data = line.split(',')

        # insert the data into the table (careful about types!)
        cur.execute('''INSERT INTO Customers VALUES(?,?,?,?,?,?,?,?,?,?,?)''',\
                    (data[0].strip(), (data[1].strip()), \
                    (data[2].strip()), (data[3].strip()),\
                    data[4].strip(), (data[5].strip()), \
                    (data[6].strip()), (data[7].strip()),\
                    data[8].strip(), (data[9].strip()), \
                    (data[10].strip())))
        
    # close the cursor
    cur.close()
    
    #commit the changes
    con.commit() 
    
    # close the connection
    con.close()         
    
def create_books(db, reader):
    '''Create and populate the Books table with
    the data from the open file data_file.'''
    
    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor
    cur = con.cursor()
    
    # Create the book table
    cur.execute('''CREATE TABLE Books(id TEXT,title TEXT,author TEXT)''')
    
   
    
    # Populate the Books Table
    # Loop through each line in the file:
    
    for line in reader:
        data = line.split(',')
        cur.execute('''INSERT INTO Books VALUES(?,?,?)''',\
                    (data[0].strip(),data[1].strip(),data[2].strip()))
                                                            
    # close the cursor
    cur.close()
    
    #commit the changes
    con.commit() 
    
    # close the connection
    con.close()     
        
def create_loans(db):
    '''Create the Loans table.'''
    
    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor
    cur = con.cursor()
    
    # Create the Loans table
    cur.execute('''CREATE TABLE Loans(CustomerID TEXT, BookID TEXT,
    BorrowedDate TEXT,DueDate TEXT, ReturnDate)''')
    
    # insert values into Loans table
    cur.execute('''INSERT INTO Loans VALUES(?,?,?,?,?)''', \
                (1, 353, 20151020, 20151030, 'NULL'))
    
    # close the cursor
    cur.close()
    
    #commit the changes
    con.commit() 
    
    # close the connection
    con.close()     
      
      
def run_query(db, query, args=None):
    '''Return the results of running query q on database db.
    If given, args contains the query arguments.'''
	
    con = sqlite3.connect(db)
    cur = con.cursor()
    if args is None:
        cur.execute(query)
    else:
        cur.execute(query, args)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data  

def get_info_by_id(db, id):
    return run_query(db, 'SELECT last_name,first_name,street_num,street_name' +
                     ' ,city,province,code,tel,alt_tel,email FROM' +
                     ' Customers WHERE id = (?)',(id,))

def get_id_by_name(db, last, first):
    return run_query(db, 'SELECT id FROM Customers WHERE last_name = (?)' + 
                     ' AND first_name = (?)', (last,first,))

def get_all_loans_by_id(db, id):
    return run_query(db, 'SELECT BookID FROM Loans WHERE CustomerID = (?)',
                     (id,))

def get_checked_out_by_id(db, id):
    return run_query(db, 'SELECT BookID FROM Loans WHERE CustomerID = (?) AND '
                     + 'ReturnDate = NULL',(id,))

def get_overdue_by_id(db, id):
    return run_query(db, 'SELECT BookID FROM Loans WHERE id = (?) AND '+
                     'ReturnDate = NULL AND ReturnDate != ' +
                     'str(datetime.now().date()).replace('-','')',(id,))


if __name__ == '__main__':

    # open the data files
    #create_customers('customers.db', open('addresses.txt'))
    #create_books('books.db', open('books.txt'))
    #create_loans('loans.db')
    db1 = 'customers.db'
    db2 = 'books.db'
    db3 = 'loans.db'
    # populate tables
    
    # close the files
    
    # call queries
    #print(get_info_by_id(db1,148))
    print(get_id_by_name(db1,'Snyder','Angel'))
    #print(get_all_loans_by_id(db3,5866))
    #print(get_checked_out_by_id(db3,1))
    #print(get_overdue_by_id(db3,2))