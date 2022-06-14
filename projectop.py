# import sql lib
# establish the connection
# check the connection.
# if connection is
# working properly  you are supposed to print data connected successfully!

# database----->
# create a db
# make a table
# make column in table also.

import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'naklibank')
cursor = con.cursor()

# if con.is_connected():
#     print("Connected Successfully!!")


# wap to print bank mang system
# take user input name,age,mobile number.


print("Bank Management System")

print("Choose any one option to banking with us!!")

while True:

    choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrwal\n4.Account Details\n5.Exit")


    if choice == '1':
        name = input("Enter your name")
        age = int(input("Enter the age"))
        mob = int(input("Enter your number"))

        # write the query to insert the person details.
        query = "insert into x values('{}',{},{})".format(name,age,mob)
        cursor.execute(query)
        con.commit()
        print("Account Open")