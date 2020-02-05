import sqlite3

conn = sqlite3.connect('part1db.db')  # Creates or opens database file

# Create a table if not exists...
conn.execute('create table if not exists Records (full_name name , country text ,catches integer)')

# Ask user for information for a new phone
full_name = input('Name of record holder (first last) ')
country = input('country represented')
catches = int(input('Enter number of catches (as an integer): '))

# Parameters. Use a ? as a placeholder for data that will be filled in
# Provide data as a second argument to .execute, as a tuple of values
conn.execute('insert into phones values (?,?, ?)', (full_name,country,catches))

conn.commit()  # Ask the database to save changes

# Fetch and display all data. Results stored in the cursor object
cur = conn.execute('select * from Records')

for row in cur:
    print(row)

conn.close()
