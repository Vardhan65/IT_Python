import MySQLdb

mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="shopdb")
print("\n Database connection established :: ",mycon)
mycon.close()