import random
raiz= None
def funcion_comp(dato1, dato2)->int:

    if dato1<dato2:
        return -1
    if dato1> dato2:
        return 1
    if dato1==dato2:
        return 0
def funcion_comp2(dato1, dato2)->int:

    if dato1!=dato2:
        return 1
    if dato1==dato2:
        return 0

def crear_arbol():
    arbol= {
            "key": None,
            "value": None,
            "right": None,
            "left": None,
            "size": 0,
            "height": 0
            }
    return arbol

def tamanio(raiz)->int:
    if (raiz is None):
        return 0
    else:
        return raiz['size']

def darAlturadelArbol(raiz)->int:
    if (raiz is None):
        return 0
    else:
        height= 1+ max(darAlturadelArbol(raiz["right"]), darAlturadelArbol(raiz["left"]))
        return height

def agregar(funcion_comp, llave, valor, raiz)->dict:
    
    if raiz == None:
        raiz= crear_arbol()
        raiz["key"]= llave
        raiz["value"]= valor


    else:
        cmp= funcion_comp(llave, raiz["key"])
        if cmp < 0:  
            raiz["left"]= agregar(funcion_comp, llave, valor, raiz["left"])
        elif cmp > 0:
            raiz["right"]= agregar(funcion_comp, llave, valor, raiz["right"])
        else: 
            raiz["value"]= valor
    
    izquierda= tamanio(raiz["left"])
    derecha= tamanio(raiz["right"])
    raiz["size"]= 1 + derecha + izquierda 
    raiz["height"]= darAlturadelArbol(raiz)
    return raiz

def borrar_arbol(raiz):

    if (raiz != None):

        if (raiz['left'] != None):

            return raiz['right']

        else:

            raiz['left'] = borrar_arbol(raiz['left'])

            raiz['size'] = tamanio(raiz['left']) + tamanio(raiz['right']) + 1

    return raiz

def elemento_min(raiz):
    izquierda = None

    if (raiz != None):
        if (raiz['left'] == None):
            izquierda = raiz
            
        else:
            izquierda = elemento_min(raiz['left'])

    return izquierda

def eliminar(funcion_comp, llave, raiz)->dict:
    if (raiz != None):
        cmp = funcion_comp(llave, raiz['key'])
        if (cmp == 0):  
            if (raiz['right'] is None):   
                return raiz['left']
            elif (raiz['left'] is None):  
                return raiz['right']
            else:      
                hijo = raiz
                raiz = elemento_min(hijo['right'])
                raiz['right'] = borrar_arbol(hijo['right'])
                raiz['left'] = hijo['left']
        elif (cmp < 0):
            raiz['left'] = eliminar(raiz['left'], llave, funcion_comp)
        else:
            raiz['right'] = eliminar(raiz['right'], llave, funcion_comp)

    raiz['size'] = 1 + tamanio(raiz['left']) + tamanio(raiz['right'])
    return raiz

def darTama??odelarbol(raiz)->int:
    return raiz["size"]

def elementos_usuario(raiz, numeros, funcion_comp)->dict:
    lista_n= random.sample(range(0, numeros), numeros)

    x=0
    while x < len(lista_n):
        raiz=agregar(funcion_comp, lista_n[x], random.randint(0, numeros), raiz)
        x+=1
    
    return raiz

def ecuacion_bool(raiz, numeros, funcion_comp)->bool:
    raiz= elementos_usuario(raiz, numeros, funcion_comp)

    if darTama??odelarbol(raiz) <= (2** darAlturadelArbol(raiz))-1 :
        return True
    else:
        return False

def nodos_nivel(raiz, nivel:int)->int:
    
    if raiz != None:
        if nivel == 0:
            return nodos_nivel(raiz["left"], nivel-1) + nodos_nivel(raiz["right"], nivel-1) + 1
        else:
            return nodos_nivel(raiz["left"], nivel-1) + nodos_nivel(raiz["right"], nivel-1)
    else:
        return 0

print(f"El resultado para la ecuacion (darTama??o(arbol) <= 2^darAlturadeArbol(arbol) - 1) para un ??rbol de 2 elementos es: {ecuacion_bool(raiz, 2, funcion_comp)}")
print(f"El resultado para la ecuacion (darTama??o(arbol) <= 2^darAlturadeArbol(arbol) - 1) para un ??rbol de 10 elementos es: {ecuacion_bool(raiz, 10, funcion_comp)}")
print(f"El resultado para la ecuacion (darTama??o(arbol) <= 2^darAlturadeArbol(arbol) - 1) para un ??rbol de 28 elementos es: {ecuacion_bool(raiz, 28, funcion_comp)}")
print(f"El resultado para la ecuacion (darTama??o(arbol) <= 2^darAlturadeArbol(arbol) - 1) para un ??rbol de 150 elementos es: {ecuacion_bool(raiz, 150, funcion_comp)}")
arbol= elementos_usuario(raiz, 150, funcion_comp)
nodos= nodos_nivel(arbol, 2)
altura = darAlturadelArbol(arbol)
print(altura)
print(nodos)