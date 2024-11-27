import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "northwind",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def ConsultarClientePA( PAIS):
    Cursor.callproc("ConsultarClientePA",(PAIS,))
    for result in Cursor.stored_results():
        print(result.fetchall())
    mydb.commit()

#frontend
CodigoClientePA = input ("ingrese codigo a consultar: ")
ConsultarClientePA (CodigoClientePA)
