#"--- TAD AREA DE INVESTIGACIÓN ---

def crearAreaDeInvestigacion():
    # Crea un área de investigación
    areainvestigacion=["", []]
    return areainvestigacion #Devuelve un area de investigacion

def cargarAreaDeInvestigacion(areainvestigacion, nombre):
    #Carga el nombre del área de investigación
    areainvestigacion[0] = nombre

def verNombreAreaInvestigacion(areainvestigacion):
    #Retorna el nombre del Area de Investigacion
    return areainvestigacion[0]
    
    
def agregarInvestigador(areainvestigacion, investigador):
    #Agrega al investigador al Área de investigacion
    areainvestigacion[1].append(investigador)


def eliminarInvestigador(areainvestigacion, investigador):
    #Elimina al investigador del Área de Investigación
    areainvestigacion[1].remove(investigador)

def existeInvestigador(areainvestigacion, investigador):
    #Retorna True o False si el investigador pertenece al Área de Investigacion
 return investigador in areainvestigacion

def tamanioAreaInvestigacion(areainvestigacion):
    #Retorna la cantidad de investigadores que hay en el Área de investigacion
    return len(areainvestigacion)

def recuperarInvestigador(areainvestigacion, i):
    #Retorna el investigador de la posición iésima
    return areainvestigacion[i]



 







