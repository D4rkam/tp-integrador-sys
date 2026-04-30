import TADareaInvestigacion
import TADInvestigador
# from TADCola import *
from datetime import date
from os import system

"""
TADInvestigador:
    - nombre: string
    - apellido: string
    - anio_de_ingreso: date
    - laboratorio: int
    - legajo: int
"""


areaQumica = TADareaInvestigacion.crearAreaDeInvestigacion()
areaBiologia = TADareaInvestigacion.crearAreaDeInvestigacion()

areas = [areaBiologia, areaQumica]

def clear():
    if system == "nt":
        system("cls")
    else:
        system("clear")

def buscarInvestigadorPorLegajo(legajo):
    for area in areas:
        for j in range(TADareaInvestigacion.tamanioAreaInvestigacion(area)):
            investigador = TADareaInvestigacion.recuperarInvestigador(area, j)
            if TADInvestigador.verNroLegajo(investigador) == legajo:
                return investigador
    return None

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
    flag = True
    while flag: 
        clear()

        legajo = int(input("Ingrese el legajo: "))
        nombre = input("Ingrese el nombre del investigador: ")
        apellido = input("Ingrese el apellido del investigador: ")
        anioIngreso = int(input("Ingrese el año de ingreso: "))
        nroLaboratorio = int(input("Ingrese el laboratorio: "))

        print("Seleccione el área de investigación:")
        for i, area in enumerate(areas):
            # 1. Area de investigacion quimica
            # 2. Area de investigacion biologia
            print(f"{i+1}. {TADareaInvestigacion.verNombreAreaInvestigacion(area)}")
        areaSeleccionada = int(input("Opción: ")) - 1
        if areaSeleccionada < 0 or areaSeleccionada >= len(areas):
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        
        nuevoInvestigador = TADInvestigador.crearInvestigador()
        TADInvestigador.cargarInvestigador(nuevoInvestigador, nombre, apellido, legajo, anioIngreso, nroLaboratorio)

        TADareaInvestigacion.agregarInvestigador(areas[areaSeleccionada], nuevoInvestigador)
        print("Investigador agregado exitosamente.")
        continuar = input("¿Desea agregar otro investigador? (s/n): ")
        if continuar.lower() != "s":
            flag = False

def interfazModificarInvestigador():
    flag = True
    while flag:
        clear()
        print("--- Modificar Investigadores ---")
        print("Ingrese el legajo del investigador a modificar:")
        legajo = int(input("Legajo: "))
        
        investigador = buscarInvestigadorPorLegajo(legajo) 
        if investigador is None:
            print("Investigador no encontrado.")
            input("Presione Enter para continuar...")
            continue

        while True:
            print(f"¿Qué dato desea modificar del investigador {TADInvestigador.verNombre(investigador)} {TADInvestigador.verApellido(investigador)}?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Año de ingreso")
            print("4. Laboratorio")

            opcion = int(input("Opción: "))

            if opcion == 1:
                nombre = input("Ingrese el nombre del investigador: ")
                TADInvestigador.modificarNombre(investigador, nombre)
            elif opcion == 2:
                apellido = input("Ingrese el apellido del investigador: ")
                TADInvestigador.modificarApellido(investigador, apellido)

            elif opcion == 3:
                anioIngreso = int(input("Ingrese el año de ingreso: "))
                TADInvestigador.modificarFechaIngreso(investigador, anioIngreso)

            elif opcion == 4:
                nroLaboratorio = int(input("Ingrese el laboratorio: "))
                TADInvestigador.modificarNroLab(investigador, nroLaboratorio)

            else: 
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue

            continuar = input("¿Desea modificar otro dato del mismo investigador? (s/n): ")
            if continuar.lower() != "s":
                break

        print("Investigador modificado exitosamente.")
        continuar = input("¿Desea modificar otro investigador? (s/n): ")
        if continuar.lower() != "s":
            flag = False

def intefazBajaPersonal():
    flag = True
    while flag:
        clear()
        print("--- Eliminar Investigadores ---")
        print("Ingrese el legajo del investigador a modificar:")
        legajo = int(input("Legajo: "))
        
        # investigador = buscarInvestigadorPorLegajo(legajo) 
        # if investigador is None:
        #     print("Investigador no encontrado.")
        #     input("Presione Enter para continuar...")
        #     continue

        eliminado = False
        for area in areas:
            i = 0
            maxLen = TADareaInvestigacion.tamanioAreaInvestigacion(area)
            while i < maxLen:
                investigadorActual = TADareaInvestigacion.recuperarInvestigador(area, i)
                if TADInvestigador.verNroLegajo(investigadorActual) == legajo:
                    TADareaInvestigacion.eliminarInvestigador(area, investigadorActual)
                    print(f"Investigador {TADInvestigador.verNombre(investigadorActual)} {TADInvestigador.verApellido(investigadorActual)} eliminado exitosamente.")
                    eliminado = True
                    break
                i += 1
            if eliminado:
                break
        if not eliminado:
            print("Investigador no encontrado.")
        
        continuar = input("¿Desea eliminar otro investigador? (s/n): ")
        if continuar.lower() != "s":
            flag = False

def intefazMostrarPlantel():
    clear()
    print("--- Plantel de Investigadores ---")
    for area in areas:
        print(f"\nÁrea de Investigación: {TADareaInvestigacion.verNombreAreaInvestigacion(area)}")
        for j in range(TADareaInvestigacion.tamanioAreaInvestigacion(area)):
            investigador = TADareaInvestigacion.recuperarInvestigador(area, j)

            print(f" - {TADInvestigador.verNombre(investigador)} {TADInvestigador.verApellido(investigador)}")
            print(f"   Legajo: {TADInvestigador.verNroLegajo(investigador)}")
            print(f"   Año de ingreso: {TADInvestigador.verFechaIngreso(investigador)}")
            print(f"   Laboratorio: {TADInvestigador.verNroLab(investigador)}")

    input("\nPresione Enter para continuar...")

def interfazReasignacionMasiva():
    clear()
    print("--- Reasignación masiva por año de ingreso ---")
    print("Seleccione el área de investigación a modificar:")


    for i, area in enumerate(areas):
        print(f"{i+1}. {TADareaInvestigacion.verNombreAreaInvestigacion(area)}")
    
    areaAModificar = -1
    while areaAModificar < 0 or areaAModificar >= len(areas):
        areaAModificar = int(input("Opción: ")) - 1

        if areaAModificar < 0 or areaAModificar >= len(areas):
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
    
    clear()

    print("Seleccione el área de investigación destino:")
    areaDestino = -1
    while areaDestino < 0 or areaDestino >= len(areas):
        for i, area in enumerate(areas):
            if i != areaAModificar:
                print(f"{i+1}. {TADareaInvestigacion.verNombreAreaInvestigacion(area)}")
        areaDestino = int(input("Opción: ")) - 1

        if areaDestino < 0 or areaDestino >= len(areas) or areaDestino == areaAModificar:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue

    anioIngreso = int(input("Ingrese el año de inicio de los investigadores a reasignar: "))

    

def interfazGenerarColaPresupuestos():
    flag = True
    while flag:
        clear()
        pass

def interfazGrafica():
    while True:
        clear()
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
