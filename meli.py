import numpy as np
'''
estado = [["*","*","*","*"],
        ["*","1","2","*"],
        ["*","3"," ","*"],
        ["*","*","*","*"]]

deseado = [["*","*","*","*"],
        ["*","1","2","*"],
        ["*"," ","3","*"],
        ["*","*","*","*"]]
'''
estado = [["*","*","*","*","*",],
            ["*","8","7","6","*"],
            ["*","5"," ","4","*"],
            ["*","3","2","1","*"],
            ["*","*","*","*","*",]]


deseado = [["*","*","*","*","*",],
            ["*","8","7","6","*"],
            ["*","5","2","4","*"],
            ["*","3","1"," ","*"],
            ["*","*","*","*","*",]]

# Lista de estados a generar
estados = []

# Toma como entrada un estado y lo imprime
def verEstado(est):
    a,b = np.shape(est)
    for i in range(0,a):
        for j in range(0,b):
            print(est[i][j], end="")
        print()

# Mover a la derecha (regresa el nuevo estado generado)
def moverDer(i,j,est):
    #print("Mov Der...",est[i][j])
    estadoN = creaNuevoEst(est)
    estadoN[i][j+1] = estadoN[i][j]
    estadoN[i][j] = " "
    return estadoN

# Mover a la izquierda (regresa el nuevo estado generado)
def moverIzq(i,j,est):
    #print("Mov Izq...",est[i][j])
    estadoN = creaNuevoEst(est)
    estadoN[i][j-1] = estadoN[i][j]
    estadoN[i][j] = " "
    return estadoN

# Mover abajo (regresa el nuevo estado generado)
def moverAba(i,j,est):
    #print("Mov Aba...",est[i][j])
    estadoN = creaNuevoEst(est)
    estadoN[i+1][j] = estadoN[i][j]
    estadoN[i][j] = " "
    return estadoN

# Mover Arriba (regresa el nuevo estado generado)
def moverAri(i,j,est):
    #print("Mov Arri...",est[i][j])
    estadoN = creaNuevoEst(est)
    estadoN[i-1][j] = estadoN[i][j]
    estadoN[i][j] = " "
    return estadoN

# Genera una matriz vacia y luego la rellena con los valores del nuevo estado generado
def creaNuevoEst(est):
    k,l = np.shape(est)
    estado = [[0 for x in range(l)] for y in range(k)]
    for i in range(0,k):
        for j in range(0,l):
            estado[i][j] = est[i][j]
    return estado

# Verifica si el nuevo estado generado ya se encuentra en la lista de estados (si no esta lo agrega)
def verifica(Nest):
    if Nest not in estados:
        estados.append(Nest)
        #print("No esta")
    else:
        #print("Si esta")
        pass

# Imprime todos los estado que se agregaron en la pila
def imprimeEstados():
    for i in estados:
        verEstado(i)
        print("-------------")
    
# Busca todos los estados posibles, verificando si la casilla vecina esta libre   
def buscaEstados(estado,n):
    #print("Buscando todos los estados para el nivel: ", n)
    k,l = np.shape(estado)
    for i in range(0,k-1):
        for j in range(0,l-1):
            if estado[i][j+1] == " " and estado[i][j] != "*":
                a = moverDer(i,j,estado)
                verifica(a)
            elif estado[i][j-1] == " " and estado[i][j] != "*":
                a = moverIzq(i,j,estado)
                verifica(a)
            elif estado[i+1][j] == " " and estado[i][j] != "*":
                a = moverAba(i,j,estado)
                verifica(a)
            elif estado[i-1][j] == " " and estado[i][j] != "*":
                a = moverAri(i,j,estado)
                verifica(a)
                
def main():
    # Para usarlo de contador durante los niveles                
    nivel = 0

    # Para tomarlo como contador del tamaño del arreglo antes de agregar nuevos estado y comenzar a generar
    # estados desde esa posicion
    tam_anterior = 0
    #Agregamos el estado inicial
    estados.append(estado)

    while True:
        aux = len(estados)
        for i in range(tam_anterior, len(estados)):
            buscaEstados(estados[i], nivel)
        nivel += 1
        tam_anterior = aux
        print("ESTAMOS EN EL NIVEL " + str(nivel) + " y el tamaño del arreglo es " + str(len(estados)))
        #imprimeEstados()
        if deseado in estados:
            print("Se encontro el estado en el nivel ", nivel)
            break
        #input("Enter para continuar...")

    imprimeEstados()



main()

