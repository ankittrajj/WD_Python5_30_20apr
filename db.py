import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'a')

cursor = con.cursor()

# if con.is_connected():
#     print('Connected successfully!!')

name = input("enter the name")
age = input("enter the age")
marks = input("entr the marks")

query = "Insert into school values ( '{}',{},{})".format(name,age,marks)
cursor.execute(query)
con.commit()
print("Data enter successfully!!")


