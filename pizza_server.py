import sqlite3
import socket
import json

conn = sqlite3.connect('pizza.db')
cursor = conn.cursor()

toppings = []
prices = {}



# to print all items in toppings table
rs = cursor.execute('select * from Toppings ')
print (rs)

# to print all items in toppings table
#for i in rs:
    #print (i)

# to print all items in prices table
for i in cursor.execute('select * from Prices'):
    print (i)

#05-03-2022

# to chnage tupples format and append to list format that application can accept (gui)
for i in cursor.execute('select * from Toppings'):
    toppings.append(i[0])

#to change tupples format of database to dictionary format that application can accept (gui)
for i in cursor.execute('select * from Prices'):
    prices[i[0]] = i[1]


cursor.close()
conn.close()

#as the host(server) it doesnt need to take any reference
host = ''

#to enable the server create a communication link on the system
port = 8685

#to create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen(5)
print (f'server started...and listening on port {port}')

# loop to connect to the client
while True:
   print(f'waiting fir connection...')
   client, addr = server.accept()
   print (f'connected to client running on address: {addr}')
   client.send(str.encode('connected to server...'))


   # loop to communicate with the client
   while True:
       req = bytes.decode(client.recv(1024))

       if req == 't':
           #serialization & unserialization
           print('sending toppings list')
           client.send(str.encode(json.dumps(toppings)))
       elif req == 'p':
           print('sending price list')
           client.send(str.encode(json.dumps(prices)))
       elif req == 'exit':
           print(f'disconnecting from client{addr}')
           break
       else:
           print('invalid request received')
           client.send(str.encode('invalid request...'))
           break