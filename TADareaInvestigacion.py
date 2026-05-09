#"--- TAD AREA DE INVESTIGACIÓN ---

def crearAreaDeInvestigacion():
    # Crea un área de investigación
    areaInvestigacion=["", []]
    return areaInvestigacion #Devuelve un area de investigacion

def cargarAreaDeInvestigacion(areaInvestigacion, nombre):
    #Carga el nombre del área de investigación
    areaInvestigacion[0] = nombre

def verNombreAreaInvestigacion(areaInvestigacion):
    #Retorna el nombre del Area de Investigacion
    return areaInvestigacion[0]


def agregarInvestigador(areaInvestigacion, investigador):
    #Agrega al investigador al Área de investigacion
    areaInvestigacion[1].append(investigador)


def eliminarInvestigador(areaInvestigacion, investigador):
    #Elimina al investigador del Área de Investigación
    areaInvestigacion[1].remove(investigador)

def existeInvestigador(areaInvestigacion, investigador):
    #Retorna True o False si el investigador pertenece al Área de Investigacion
 return investigador in areaInvestigacion[1]

def tamanioAreaInvestigacion(areaInvestigacion):
    #Retorna la cantidad de investigadores que hay en el Área de investigacion
    return len(areaInvestigacion[1])

def recuperarInvestigador(areaInvestigacion, i):
    #Retorna el investigador de la posición iésima
    return areaInvestigacion[1][i]



 







