# ==== Crear ====
def crearInvestigador():
    """Crea y retorna investigador vacio"""
    return ["", "", 0, "", 0]


# ==== Carga de datos ====
def cargarInvestigador(
    investigador, nombre, apellido, num_legajo, fecha_ingreso, num_lab
):
    """
    Recibe un investigador y los datos a ser cargados:
    - Nombre
    - Apellido
    - Numero de legajo
    - Fecha de ingreso
    - Numero de laboratorio
    """
    investigador[0] = nombre
    investigador[1] = apellido
    investigador[2] = num_legajo
    investigador[3] = fecha_ingreso
    investigador[4] = num_lab


# ==== Ver datos ====
def verNombre(investigador):
    """Recibe un investigador y retorna su nombre"""
    return investigador[0]


def verApellido(investigador):
    """Recibe un investigador y retorna su apellido"""
    return investigador[1]


def verNroLegajo(investigador):
    """Recibe un investigador y retorna su numero de legajo"""
    return investigador[2]


def verFechaIngreso(investigador):
    """Recibe un investigador y retorna su fecha de ingreso"""
    return investigador[3]


def verNroLab(investigador):
    """Recibe un investigador y retorna su numero de laboratorio"""

    return investigador[4]


# ==== Modificar datos ====
def modificarNombre(investigador, nombre):
    """Recibe un investigador y modifica el nombre al nuevo recibido"""

    investigador[0] = nombre


def modificarApellido(investigador, apellido):
    """Recibe un investigador y modifica el apellido al nuevo recibido"""

    investigador[1] = apellido


def modificarNroLegajo(investigador, num_legajo):
    """Recibe un investigador y modifica el numero de legajo al nuevo recibido"""

    investigador[2] = num_legajo


def modificarFechaIngreso(investigador, fecha_ingreso):
    """Recibe un investigador y modifica la fecha de ingreso al nuevo recibido"""

    investigador[3] = fecha_ingreso


def modificarNroLab(investigador, num_lab):
    """Recibe un investigador y modifica el numero de laboratorio al nuevo recibido"""

    investigador[4] = num_lab


def asignarInvestigador(investigador1, investigador2):
    """Copia los datos del investigar 1 al investigador 2"""

    investigador2[0] = investigador1[0]
    investigador2[1] = investigador1[1]
    investigador2[2] = investigador1[2]
    investigador2[3] = investigador1[3]
    investigador2[4] = investigador1[4]
