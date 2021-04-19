import csv
from ClassEmail import Email


if __name__== '__main__':
    
    unMail = Email()
    unMail.retornaEmail()
    unMail.cambioContrasena()
    unMail.crearCuenta(input("ingrese correo: "))
    archivo = open("archivo.csv")
    reader = csv.reader(archivo, delimiter = ",")
    dominio=input("ingrese dominio a buscar: ")
    cont=0
    for fila in reader:
       if fila[1] == dominio:
            cont = cont + 1
    archivo.close()
    print("el dominio se repite",cont,"veces")