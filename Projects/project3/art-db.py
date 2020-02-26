import sqlite3

# create customer data base

def make_cust_db():
    connection = sqlite3.connect('artists_db')

    # cursor
    crsr = connection.cursor()

    # SQL command to create a table in the database
    sql_command = """if not exists CREATE TABLE artists ( 
    cust_ID_num INTEGER PRIMARY KEY, 
    fullname VARCHAR(60), 
    email VARCHAR(50);"""

    # execute the statement
    crsr.execute(sql_command)

    # SQL command to insert the data in the table
    sql_command = """INSERT INTO artists VALUES (1,"Rishabh Bansal",
    "Rishabh.Bansal@gmoal.com ");"""
    crsr.execute(sql_command)

    # another SQL command to insert the data in the table
    sql_command = """INSERT INTO artists VALUES (2, "Bill Gates", 
    "Bill.Gates@gmoal.com");"""
    crsr.execute(sql_command)

    # To save the changes in the files.
    # If we skip this, nothing will be saved in the database.
    connection.commit()

    # close the connection
    connection.close()


#create dbsqlite3.connect('artworkdb')



def makw_art_work_db():
    conn = sqlite3.connect('artwork')

    sql_command = """create table if not exists artwork ( 
    item_ID_num INTEGER PRIMARY KEY, 
    artist  VARCHAR(50), 
    title VARCHAR(30), 
    price int 
    );"""
    conn.execute(sql_command)
    
    conn.execute('insert into artwork values (1,"Pablo Piccaso","Sunflowers",2000000)')
    conn.execute('insert into artwork values (2,"Rachel Hoover", "Kissing '
                 'People",35000)')
    conn.execute('insert into artwork values (3,"Joe Huber", "BanjoMan",43000)')
    conn.execute('insert into artwork values (4,"Banksy", "Big Jon",'
                 '78000)')
    
    conn.commit()  # Finalize updates
    
    for row in conn.execute('select * from artwork'):
        print(row)
    #
    # conn.execute('drop table artwork')  # Delete table
    
    conn.commit()  # Ask the database to save changes - don't forget!
    
    conn.close()  # And close connection.