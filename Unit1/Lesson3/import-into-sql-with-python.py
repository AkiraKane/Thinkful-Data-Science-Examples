# import the sql library into python
import sqlite3 as lite

# data to be inserted into tables stored as tuples with-in a tuple
cities = (('Boston', 'MA'),
('Chicago', 'IL'),
('Miami', 'FL'),
('Dallas', 'TX'),
('Seattle', 'WA'),
('Portland', 'OR'),
('San Francisco', 'CA'),
('Los Angeles', 'CA'))

weather = (('Boston', '2013', 7, 1, 59, 0),
('Chicago', '2013', 7, 1, 59, 0),
('Miami', '2013', 8, 1, 84, 0),
('Dallas', '2013', 7, 1, 77, 0),
('Seattle', '2013', 7, 1, 61, 0),
('Portland', '2013', 7, 12, 63, 0),
('San Francisco', '2013', 9, 12, 64, 0),
('Los Angeles', '2013', 9, 12, 75, 0))

# connect to your SQL database and store as a variable to call in future code
con = lite.connect('my_database.db')

with con:
    # setup the cursor for accessing records in the tables
    cur = con.cursor()

    '''
        INSERTING DATA INTO SQLITE DATABASE
    '''
    # sqlite3 versions 3.6 and up use something like the following code
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?,?)", weather)

    # # sqlite3 versions 3.5 and below use something like the following code
    # for rec in cities:
    #     cur.execute("INSERT INTO cities VALUES (\'"+rec[0]+"\',\'"+rec[1]+"\')")
    # for rec in weather:
    #     cur.execute("INSERT INTO weather VALUES (\'"+rec[0]+"\',"+str(rec[1])+","+str(rec[2])+","+str(rec[3])+","+str(rec[4])+")")

    '''
        RETRIEVING RAW DATA FROM SQLITE DATABASE
    '''
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print row

    '''
        RETRIEVING DATA FROM DATABASE AND STORING IT IN A PANDAS DATAFRAME
    '''
    # import the pandas library
    import pandas as pd
    # Select all rows
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    # set column labels from the first row of data retieved from the DB
    cols = [desc[0] for desc in cur.description]
    # set the pandas dataframe with data and column labels
    df = pd.DataFrame(rows, columns=cols)
    # display the first bit of data from the pandas DataFrame
    print df.head()

