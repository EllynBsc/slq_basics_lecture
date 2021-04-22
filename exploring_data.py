import sqlite3


 # WITH PYHTON BASICS:

# conn = sqlite3.connect('data/soccer.sqlite')
# c = conn.cursor()

# c.execute("SELECT * FROM Country")
# execute('SQL QUERY')

# rows = c.fetchall() #list of tuples

# print(rows)
# print(type(rows))

# for row in rows:
#   print(row[0], row[1])


# WITH PYTHON ADVANCED:

conn = sqlite3.connect('data/soccer.sqlite')
conn.row_factory = sqlite3.Row #magic line, allows you to access the rows with the name of the column
c = conn.cursor()

# c.execute("SELECT * FROM Country")
# rows = c.fetchall()

# print(rows)
# print(type(rows))

# for row in rows:
#   print(row['name'], row['id'])
#   print(row[1], row[0])


# FETCH ONE ROW:

c.execute("SELECT * FROM Country WHERE Country.id = 1")
row = c.fetchone()

print(row['name'])
