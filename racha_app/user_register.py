import mysql.connector
from dbcon import connect
from passlib.hash import sha256_crypt

c, conn = connect()
 
data = ('admin', 'Matheus', 'No email', sha256_crypt.hash('#Rachadjzao115'))

add_admin = ("INSERT INTO users (user, username, email, password) VALUES (%s, %s, %s, %s)")

c.execute(add_admin, data)

conn.commit()

c.close()
conn.close()