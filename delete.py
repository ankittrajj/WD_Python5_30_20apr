import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'a')

cursor = con.cursor()

age = int(input("enter the age"))

query = "delete from school where age = '{}'".format(age)
cursor.execute(query)
con.commit()
print("delete successfully!!")