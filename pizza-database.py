import sqlite3

#to create database file and connect to database
conn = sqlite3.connect('pizza.db')

#to create a cursor
cursor = conn.cursor()

#varchar is variable character
#cursor.execute('create table Toppings(name varchar(15) primary key)')

#insert content in table
#cursor.execute("insert into Toppings(name) values('Chicken')")


#2nd class
# to insert multiple entries into  a column
#toppings = [('onion',), ('Green-pepper',), ('red-pepper',), ('black-olive',), ('mushroom',)]

#stmt1 = "insert into Toppings values (?)"
#cursor.executemany(stmt1, toppings)

# to create a data list for prices table
#prices = [('medium',3000),('large',5000),('xlarge',7500),
          #('sausage',3000),('pepperoni',150),('chicken',550),('mushroom',250),
          #('black oilve',200),('green pepper',100),('red pepper',50),('onion',250)
          #]

#stmt2 = 'insert into Prices values (?, ?)'
#code on how to update a data on the database
#cursor.execute("update Prices set price=350 where product='onion'")


#cursor.execute('create table Prices(product varchar(15) primary key, price decimal(10, 2))')
#cursor.executemany(stmt2, prices)




conn.commit()
cursor.close()
conn.close()