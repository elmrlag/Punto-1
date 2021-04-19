class Email:
    __idCuenta=str
    __dominio=str
    __tDominio=str
    __contrasena=str
    
    def __init__(self,v1="MatiasCastro",v2="gmail",v3="com",v4="gokudios"):
        self.__idCuenta=v1
        self.__dominio=v2
        self.__tDominio=v3
        self.__contrasena=v4

    def retornaEmail(self):
        print("Ingrese los siguientes datos")
        nombre = input("Nombre: ")
        self.__idCuenta = input ("Id de la cuenta: ")
        self.__dominio = input ("Dominio de la cuenta: ")
        self.__tipoDominio = input ("Tipo de dominio de la cuenta: ")
        self.__contrasena = input ("Contrasena: ")
        print("Estimado",nombre,"te enviaremos tus mensajes a la dirección ",self.__idCuenta,"@",self.__dominio,".",self.__tipoDominio)
    
    def getContrasena(self):
        return(self.__contrasena)
    
    def cambioContrasena(self):
        x=input("ingrese contraseña actual: ")
        if (x==self.__contrasena):
            x=input("ingrese nueva contraseña: ")
            self.__contrasena=x
        else:
             print("contraseña incorrecta")
    
    def getDominio(self):
        return(self.__dominio)

    def crearCuenta(self,correo):
        import re
        #correo = re.split(r'@|\.', correo)
        correo = correo.split("@")
        self.__idCuenta=correo[0]
        print("La ID es:",correo[0])
        correo[0]=correo[1]
        correo.pop()
        correo="".join(correo)
        correo = correo.split(".",1)
        print("El dominio es:", correo[0])
        print("El tipo de dominio es:", correo[1])
        self.__dominio=correo[0]
        self.__tDominio=correo[1]

