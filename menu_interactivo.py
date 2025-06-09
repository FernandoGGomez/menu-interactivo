import time, random

arbol = ["Menu Principal", ["1_ Consulta de saldo", ["1_ Consultar saldo cuenta corriente"], ["2_ Consultar saldo cuenta ahorro"]], ["2_ Retiro de efectivo", ["1_ Retirar 20 mil pesos"], ["2_ Retirar un monto especifico"]], ["3_ Depositos",["1_ Depositar en efectivo",], ["2_ Depositar en sobre"]], ["4_ Transferencias", ["1_ Transferir a un alias"], ["2_ Transferir a un CBU/CVU"]], ["5_ Cambiar de clave", ["1_Cambiar clave del cajero"], ["2_Cambiar clave del home banking"]]]

while True:

    print("Bienvenido al banco")
    for submenu in arbol[1:]:
        print(submenu[0])
    
    eleccion = input("Por favor, seleccione una opcion: ")

    if(eleccion == "1"):
        print(f"{arbol[1][1][0]}\n{arbol[1][2][0]}")
        eleccion = input("Por favor, seleccione una opcion: ")
        if (eleccion == "1"):
            print(f"Su saldo es de {random.randint(10000,100000)} pesos")
        else:
            print(f"Su saldo es de {random.randint(5000,10000)} pesos")
    elif(eleccion == "2"):
        print(f"{arbol[2][1][0]}\n{arbol[2][2][0]}")
        eleccion = input("Por favor, seleccione una opcion: ")
        if (eleccion == "1"):
            print("Usted retiro 20 mil pesos.")
        else:
            monto = input("Ingrese el monto a retirar: ")
            print(f"Usted retiro {monto} pesos de manera exitosa.")
    elif(eleccion == "3"):
        print(f"{arbol[3][1][0]}\n{arbol[3][2][0]}")
        eleccion = input("Por favor, seleccione una opcion: ")
        if (eleccion == "1"):
            print("Ingrese el dinero por la boquilla del cajero")
            time.sleep(3)
            print("Se ingreso el dinero de manera exitosa")
        else:
            print("Ingrese el sobre por la boquilla del cajero")
            time.sleep(3)
            print("Se ingreso el dinero de manera exitosa")
    elif(eleccion == "4"):
        print(f"{arbol[4][1][0]}\n{arbol[4][2][0]}")
        eleccion = input("Por favor, seleccione una opcion: ")
        if (eleccion == "1"):
            alias = input("Ingrese el alias: ")
            monto = input("Ahora ingrese el dinero a transferir: ")
            print(f"Se ha realizado la transferncia con exito al alias: {alias} con un monto total de {monto} pesos")
        else:
            cbu = input("Ingrese el alias: ")
            monto = input("Ahora ingrese el dinero a transferir: ")
            print(f"Se ha realizado la transferncia con exito al cbu: {cbu} con un monto total de {monto} pesos")
    elif(eleccion == "5"):
        print(f"{arbol[5][1][0]}\n{arbol[5][2][0]}")
        eleccion = input("Por favor, seleccione una opcion: ")
        if (eleccion == "1"):
            input("Ingrese la nueva contraseña para usar el cajero: ")
            print("La contraseña se cambio con exito")
        else:
            input("Ingrese la nueva contraseña para usar su home banking: ")
            print("La contraseña se cambio con exito")
    else:
        print("Opcion invalida")
    
    continuar = input("Desea realizar otra operacion? (s/n)").lower()
    if continuar != "s":
        print("Gracias por usar el cajero, vuelva pronto.")
        break
    
