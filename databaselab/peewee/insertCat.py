import sqlite3

conn = sqlite3.connect('cat.sqlite')  # Creates or opens database file

# Create a table if not exists...
conn.execute('create table if not exists cat (name name , color text ,age integer)')

# Ask user for information for a new phone
name = input('Name of Cat ')
color = input('color of cat')
age = int(input('Enter age of the cat (as an integer): '))

# Parameters. Use a ? as a placeholder for data that will be filled in
# Provide data as a second argument to .execute, as a tuple of values
conn.execute('insert into cat values (?,?, ?)', (name,color,age))

conn.commit()  # Ask the database to save changes

# Fetch and display all data. Results stored in the cursor object
cur = conn.execute('select * from cat')

for row in cur:
    print(row)

conn.close()
