import mysql.connector

# Connection Values
mydb = mysql.connector.connect(
    host='127.6.3.1',
    user='Capstone1',
    password='Capstone1',
    database='E-store'
)

# Cursor object
mycursor = mydb.cursor()

# Queries
sql = "Select * FROM users"

# execute query
mycursor.execute(sql)

# Fetch Queries
myresult = mycursor.fetchall()

# Print results
for row in myresult:
    print(row)

#close connection    
mycursor.close()
mydb.close() 