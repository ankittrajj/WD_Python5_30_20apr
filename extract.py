import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database = 'emp')

cursor = con.cursor()
query = 'select * from sal'
cursor.execute(query)

# data = cursor.fetchone()
# data1 = cursor.fetchmany(2)
data2 = cursor.fetchall()
print(data2)

# one ---- fetch only one data
# many-----> fetch more than or one data
# all ----> fetch all data.