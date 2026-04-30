# === crear cola ===
def crearCola():
    cola = []
    return cola

# === Encolar ===
def encolar(cola, elem):
    #agrega un elemento al final de la cola
    cola.append(elem)
        
# === desencolar ===
def desencolar(cola):
    #retorna y elimina el primer elemento de la cola
    return cola.pop(0)

# === cola Vacia ===
def colaVacia(cola):
    #retorna verdadero si la cola es vacia
    return len(cola) == 0    

# === contar elementos ===
def tamanioCola(cola):
    #retorna la cantidad de los elementos de la cola
    return len(cola)

# === copiar cola ===
def copiarCola(cola1, cola2):
    #Copia los datos de la cola 2 a la cola 1
    aux = crearCola()
    while not colaVacia(cola2):
        elem = desencolar(cola2)
        encolar(aux, elem)
    while not colaVacia(aux):
        elem = desencolar(aux)
        encolar(cola1, elem)
        encolar(cola2, elem)
