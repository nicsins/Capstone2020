import sqlite3



conn = sqlite3.connect('part1db')

conn.execute('create table if not exists Records (full_name name , country text ,catches integer)')

conn.execute('insert into Records values ("Janne Mustonen", "Finland",98)')
conn.execute('insert into Records values ("Ian Stewart", "Canada",94)')
conn.execute('insert into Records values ("Aaron Gregg", "Canada",88)')
conn.execute('insert into Records values ("Chad Taylor", "USA",78)')

conn.commit()  # Finalize updates

for row in conn.execute('select * from Records'):
    print(row)
#
# conn.execute('drop table phones')  # Delete table

conn.commit()  # Ask the database to save changes - don't forget!

conn.close()  # And close connection.


