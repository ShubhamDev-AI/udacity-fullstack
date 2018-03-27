# Python DB Api

## `psql`

To connect `psql` to a database running on the same machine (such as your VM), all you need to give it is the database name. For instance, the command `psql forum` will connect to the `forum` database.

From within `psql`, you can run any SQL statement using the tables in the connected database. Make sure to end SQL statements with a semicolon, which is not always required from Python.

### Commands

 - `\d {table}`: display the columns of the table.
 - `\dt`: list all the tables in the database.
 - `\dt+`: list tables plus additional information (notably, how big each table is on disk).
 - `\H`: switch between printing tables in plain text vs. HTML.
 - `{query} \watch`: Repeatedly execute the current query buffer
 - `\q`: Quit psql

[Commands Ref](https://www.postgresql.org/docs/9.4/static/app-psql.html)




## Python Examples:

Execute a select:

```py

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()


```

Insert a row:

```py

import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()


```