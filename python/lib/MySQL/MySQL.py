import mysql.connector as s
mydb = s.connect(
    host = 'localhost',
    user = 'hanrker',
    password = '123123',
    auth_plugin='mysql_native_password'
)
print(mydb)