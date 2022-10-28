from re import I
lista= [
        {"artista":"luciano pereyra","nombretema":"en tus manos","letra":"Será difícil llegar;Pero con esperanza El destino en tus manos está"},
        {"artista":"soledad pastorutti","nombretema":"tren del cielo","letra":"Viajo por las nubes Voy llevando mi canción"},
        {"artista":"abel pintos","nombretema":"ya estuve aqui","letra":"Es inevitable el sentir, Que cruzan puentes entre tu abrazo"},
        {"artista":"axel","nombretema":"celebra la vida","letra":"no se si soñaba, no se si dormia"},
        {"artista":"airbag","nombretema":"solo aqui","letra":"solo aqui,sentado sin saber,que hacer,yo se que estas con el"} #punto1)
]

def imprimlistado(): #punto2)
    for i in lista:
        print("*",i["artista"],"--",i["nombretema"])
        
    textMenu()

def agregarElemento():#punto3)
    nuevotema = {"artista": "", "nombretema": "", "letra": ""}
    nuevotema["artista"] = input("ingrese nombre del artista: ")
    nuevotema["nombretema"] = input("ingrese nombre del tema: ")
    nuevotema["letra"]= input("ingrese letra: ")
    lista.append(nuevotema)
    print(lista)
    
    textMenu()
    
def buscartema(): #punto 4)
    nombretema = input("ingrese nombre del tema:")
    
    encontrado = False
    for elemento in lista:
        if nombretema == elemento["nombretema"]:
            encontrado = True
            elementoEncontrado = elemento

    if encontrado == True:
        print("tema encontrado: ",elementoEncontrado["nombretema"], "-",elementoEncontrado["artista"])
    else:
        print("no se encontro el tema")

    textMenu()

def modificarcancion(): #punto 5
    cancionBuscada = input("escriba el nombre de la cancion que desea modificar:")
    
    for cancion in lista:

        if cancion["nombretema"] == cancionBuscada:
            datonuevo =input("que dato desea modificar:(escriba la palabra)\n(1-artista)\n(2-nombre del tema)\n(3-letra)\n(4-salir)\nopcion:")
            
            if datonuevo == "artista":
                artistanuevo = input("ingrese nuevo nombre/dato del artista: ")
                cancion["artista"] = artistanuevo
                print("*","artista",cancion["artista"],"/",cancionBuscada)
                imprimlistado()

            if datonuevo == "nombre del tema":  
                nombretema =input("ingrese nuevo nombre tema: ")
                cancion["nombretema"] = nombretema
                print("artista",cancionBuscada,"/",cancion["nombretema"])
                imprimlistado()

            if datonuevo == "letra":    
                letra = input("ingrese nueva letra: ")
                cancion["letra"]= letra
                print("*","artista",cancionBuscada,"/","nombretema:",cancion["nombretema"])
                imprimlistado()

            if datonuevo == "salir":
                textMenu() 
        else:
            print("error")


    textMenu()
        
def textMenu(): #punto 6
    print("Elija una opcion del siguiente menu:")
    print('1)- lista de canciones: opcion 1')
    print('2)- buscar cancion: opcion 2')
    print('3)- modificar cancion: opcion 3')
    print('4)- agregar cancion: opcion 4')
    print('5)- salir = 5:')
    eleccion = int(input())
    if eleccion == 1:
       imprimlistado()
    elif eleccion == 2:
        buscartema()
    elif eleccion == 3:
        modificarcancion()
    elif eleccion == 4:
        agregarElemento()
    elif eleccion == 5:
        print("fin del menu")
    else:
        print('opcion no valida')
        textMenu()
textMenu()