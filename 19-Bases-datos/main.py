from unittest import result
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

#print(database)

cursor = database.cursor()


# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")
"""


# Crear tabla
cursor.execute("""
create table if not exists vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    constraint pk_vehiculo primary key(id)
    )
""")

for bd in cursor:
    print(bd)



# Insertar registros
#cursor.execute("insert into vehiculos values(null, 'Nissan', 'Versa', 289000)")
#database.commit()

cursor.execute("Select * from vehiculos")
result = cursor.fetchall()

for carro in result:
    print(carro)

cursor.execute("delete from vehiculos where modelo = 'Versa'")

print(cursor.rowcount, "borrados!!!")

