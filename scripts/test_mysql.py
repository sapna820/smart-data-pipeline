import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_dw",
    auth_plugin="mysql_native_password"
)

print("Connection SUCCESS")
conn.close()