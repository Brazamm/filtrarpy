import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "northwind",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def ConsultarCliente( codigo):
    Cursor.callproc("ConsultarCliente: ",(codigo,))
    for result in Cursor.stored_results():
        print(result.fetchall())
    mydb.commit()

#frontend
CodigoCliente = input ("ingrese codigo a consultar: ")
ConsultarCliente (CodigoCliente)
