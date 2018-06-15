# SQLite is built into sublime and its good for small databases
import sqlite3

# setup a connection to SQLite. This will automatically create the database employee.db
# Here you could also use ':memory:' to make a database in memory
conn = sqlite3.connect('employee.db')

# create a cursor that allows you to make SQL commands
c = conn.cursor()

# here is the SQL code to execute. The triple brackets is called a doc string, it allows you to make a string across 
# multiple lines

# c.execute("""CREATE TABLE employees (
# 				first text,
# 				last text,
# 				pay int
# 	)""")

#note: after you initially create the database(table) you need to get rid of
# that bit of code, it will throw an error if you try to create the same table 
#twice

# play around with the database
#c.execute("INSERT INTO employees VALUES ('Brian', 'Hen', 500)")
#conn.commit()

c.execute("SELECT * FROM employees WHERE last= 'Hen'")

#this gets the next row in results
#print(c.fetchone())

# this gets all the rows in a list
print(c.fetchall())

#this commits the command not the 'c', it is easy to forget
conn.commit()

#make sure to end by closing the connection
conn.close()
