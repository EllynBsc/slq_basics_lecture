SQL BASICS

1. Databases
  #1.1: relational databases
  #1.2: SQlite: DB stored in one file.

2.METHODOLOGY:
  #2.1: Find a dataset/database to play with on kaggle. This should be a sqlite file.
  #2.2: DBEAVER as a software to open it. I cannot double click on a sqlite file. Works on windows, linux & MAC.
  #2.3: EXPLORE THE ERD Diagram with : kitt.lewagon.com/db

# Download and install DBeaver, a free and open source powerful tool to connect to any database, explore the schema and even run SQL queries.
3.Querying the Database
  # 3.1: With DBeaver: Select * from country. You can export as csv.
  # 3.2: With Python basics. How to do sql with python ? That's the idea if you don't want to use GUI.
    # we need sqlite3 package included in python 3
    # fetchall
  # 3.3 : With Python advanced
    #sqlite3Row to access the rows with the name of the column
  # 3.4: Fetching only one element.
    # fetch one

4.SQL
# How to go from plain english to a SQL query ?
  # 4.1: Projection - Choosing which columns the query shall return.
    => SELECT
  # 4.2: Selection - Selecting which rows the query shall return.
    => WHERE #boolean condition/algebra => where not, or => python algebra is the same in Sql.
    #I can use WHERE in (list_of_values)
  # 4.3: Counting - Counting the number of rows matching the selection
    => COUNT
  # 4.4: Sorting - Sorting the rows based on a column (or a group of columns)
    => ORDER BY
  # 4.5: Grouping - Grouping rows on a given column C (aggregating rows with a function where values of C column are the same)
    => GROUP BY
  # 4.6: Querying multiple tables with JOIN
    => JOIN


Objectives of the day:

# -Explore a new database and draw its schema with kitt.lewagon.com/db
# -Query the database with SQL with a GUI client like DBeaver
# -Use Python to execute SQL queries against the database

Jargon of the day:
# -table
# -columns
# -rows
# -schema
# -primary_key
# -foreign_key
# -relationship
# -query in Sql



# HEREDOC

# query = """
#       SELECT *
#       FROM country

# """
# db.execute(query)











































