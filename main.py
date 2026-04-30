import TADareaInvestigacion
import TADInvestigador
# from TADCola import *
from datetime import date

"""
TADInvestigador:
    - nombre: string
    - apellido: string
    - ano_de_ingreso: date
    - laboratorio: int
    - legajo: int
"""

areaQumica = crearAreaDeInvestigacion()
areaBiologia = crearAreaDeInvestigacion()

areas = [areaBiologia, areaQumica]

def buscarInvestigadorPorLegajo(legajo):
    return 

def menuPrincipal():
    print("\n--- Menú Principal ---")
    print("1. Agregar investigador")
    print("2. Modificar investigador")
    print("3. Baja de personal")
    print("4. Mostrar plantel de investigadores")
    print("5. Reasignación masiva por año de ingreso")
    print("6. Generar cola para presupuestos anuales")
    print("7. Salir")
    
    return int(input("Seleccione una opción: "))

def interfazAgregarInvestigador():
    legajo = int(input("Ingrese el legajo: "))
    nombre = input("Ingrese el nombre del investigador: ")
    apellido = input("Ingrese el apellido del investigador: ")
    anoIngreso = int(input("Ingrese el año de ingreso: "))
    laboratorio = input("Ingrese el laboratorio: ")

    print("Seleccione el área de investigación:")
    for i, area in enumerate(areas):
        print(f"{i+1}. {TADareaInvestigacion.verNombre(area)}")
    areaSeleccionada = int(input("Opción: ")) - 1
    
    nuevoInvestigador = TADInvestigador.crearInvestigador()
    TADInvestigador.cargarInvestigador(nuevoInvestigador, nombre, apellido, legajo, anoIngreso, laboratorio)

    # TADareaInvestigacion(areas[areaSeleccionada], )
    return

def interfazModificarInvestigador():
    print("Ingrese el legajo del investigador a modificar:")
    legajo = int(input("Legajo: "))
    
    investigador = buscarInvestigadorPorLegajo(legajo) 
    nombre = input("Ingrese el nombre del investigador: ")
    apellido = input("Ingrese el apellido del investigador: ")
    area = input("Ingrese el área de investigación: ")
    anoIngreso = int(input("Ingrese el año de ingreso: "))
    laboratorio = input("Ingrese el laboratorio: ")

    return

def intefazBajaPersonal():
    return

def intefazMostrarPlantel():
    return

def interfazReasignacionMasiva():
    return

def interfazGenerarColaPresupuestos():
    return

def interfazGrafica():
    while True:
        opcion = menuPrincipal()
        
        if opcion == 1:
            interfazAgregarInvestigador()
        elif opcion == 2:
            interfazModificarInvestigador()
        elif opcion == 3:
            intefazBajaPersonal()
        elif opcion == 4:
            intefazMostrarPlantel()
        elif opcion == 5:
            interfazReasignacionMasiva()
        elif opcion == 6:
            interfazGenerarColaPresupuestos()
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    return

def main():
    interfazGrafica()
    return

if __name__ == "__main__":
    main()
