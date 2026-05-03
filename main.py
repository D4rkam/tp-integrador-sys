import TADareaInvestigacion as TADai
import TADInvestigador as TADi
# from TADCola import *
from datetime import date
import os
import platform

"""
TADInvestigador:
    - nombre: string
    - apellido: string
    - fecha_de_ingreso: date
    - laboratorio: int
    - legajo: int
"""


areaQumica = TADai.crearAreaDeInvestigacion()
areaBiologia = TADai.crearAreaDeInvestigacion()
TADai.cargarAreaDeInvestigacion(areaQumica, "Química")
TADai.cargarAreaDeInvestigacion(areaBiologia, "Biología")

areas = [areaBiologia, areaQumica]
colas = {}

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def buscarInvestigadorPorLegajo(legajo):
    for area in areas:
        for j in range(TADai.tamanioAreaInvestigacion(area)):
            investigador = TADai.recuperarInvestigador(area, j)
            if TADi.verNroLegajo(investigador) == legajo:
                return investigador
    return None

def menuPrincipal():
    print("\n--- Menú Principal ---")
    print("1. Agregar investigador")
    print("2. Modificar investigador")
    print("3. Baja de personal")
    print("4. Mostrar plantel de investigadores")
    print("5. Reasignación masiva por año de ingreso")
    print("6. Cola para presupuestos anuales")
    print("7. Salir")    
    return input("Seleccione una opción: ")

def interfazAgregarInvestigador():
    flag = True
    while flag: 
        clear()
        print("--- Agregar Investigadores ---")

        try:
            print("Seleccione el área de investigación:")
            for i, area in enumerate(areas):
                # 1. Area de investigacion quimica
                # 2. Area de investigacion biologia
                print(f"{i+1}. {TADai.verNombreAreaInvestigacion(area)}")
            areaSeleccionada = int(input("Opción: ")) - 1
            if areaSeleccionada < 0 or areaSeleccionada >= len(areas):
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue

            legajo = int(input("Ingrese el legajo: "))
            nombre = input("Ingrese el nombre del investigador: ")
            apellido = input("Ingrese el apellido del investigador: ")
            nroLaboratorio = int(input("Ingrese el n° de laboratorio: "))

            anioIngreso = int(input("Ingrese el año de ingreso: "))
            mesIngreso = int(input("Ingrese el mes de ingreso: "))
            diaIngreso = int(input("Ingrese el día de ingreso: "))
            fechaIngreso = date(anioIngreso, mesIngreso, diaIngreso)
        except ValueError as ve:
            print(f"Opción no válida. Intente nuevamente. {ve}")
            input("Presione Enter para continuar...")
            continue
        except Exception as e:
            print(f"Error: {e}. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
            
        nuevoInvestigador = TADi.crearInvestigador()
        TADi.cargarInvestigador(nuevoInvestigador, nombre, apellido, legajo, fechaIngreso, nroLaboratorio)

        TADai.agregarInvestigador(areas[areaSeleccionada], nuevoInvestigador)
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
            print(f"¿Qué dato desea modificar del investigador {TADi.verNombre(investigador)} {TADi.verApellido(investigador)}?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Fecha de ingreso")
            print("4. Laboratorio")

            opcion = int(input("Opción: "))

            if opcion == 1:
                nombre = input("Ingrese el nombre del investigador: ")
                TADi.modificarNombre(investigador, nombre)
            elif opcion == 2:
                apellido = input("Ingrese el apellido del investigador: ")
                TADi.modificarApellido(investigador, apellido)

            elif opcion == 3:
                try:
                    anioIngreso = int(input("Ingrese el año de ingreso: "))
                    mesIngreso = int(input("Ingrese el mes de ingreso: "))
                    diaIngreso = int(input("Ingrese el día de ingreso: "))
                    fechaIngreso = date(anioIngreso, mesIngreso, diaIngreso)
                    TADi.modificarFechaIngreso(investigador, fechaIngreso)
                except ValueError:
                    print("Fecha no válida. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    continue
                except Exception as e:
                    print(f"Error: {e}. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    continue

            elif opcion == 4:
                nroLaboratorio = int(input("Ingrese el n° de laboratorio: "))
                TADi.modificarNroLab(investigador, nroLaboratorio)

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
            maxLen = TADai.tamanioAreaInvestigacion(area)
            while i < maxLen:
                investigadorActual = TADai.recuperarInvestigador(area, i)
                if TADi.verNroLegajo(investigadorActual) == legajo:
                    TADai.eliminarInvestigador(area, investigadorActual)
                    print(f"Investigador {TADi.verNombre(investigadorActual)} {TADi.verApellido(investigadorActual)} eliminado exitosamente.")
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

def imprimirPlantelArea(area):
    print(f"\nÁrea de Investigación: {TADai.verNombreAreaInvestigacion(area)}")
    if TADai.tamanioAreaInvestigacion(area) == 0:
        print("No hay investigadores en esta área.")
        input("Presione Enter para continuar...")
        return
    print(f"{"":<3} {'Nombre y apellido':<25} {'Legajo':<10} {'Año de ingreso':<15} {'Laboratorio':<10}")
    for j in range(TADai.tamanioAreaInvestigacion(area)):
        investigador = TADai.recuperarInvestigador(area, j)
        nombre = TADi.verNombre(investigador) + " " + TADi.verApellido(investigador)
        legajo = TADi.verNroLegajo(investigador)
        fechaDeIngreso = f"{TADi.verFechaIngreso(investigador).day}/{TADi.verFechaIngreso(investigador).month}/{TADi.verFechaIngreso(investigador).year}"
        nroLaboratorio = TADi.verNroLab(investigador)
        print(f"{j+1:<3} {nombre:<25} {legajo:<10} {fechaDeIngreso:<15} {nroLaboratorio:<10}")

def intefazMostrarPlantel():
    clear()
    print("--- Plantel de Investigadores ---")

    for area in areas:
        imprimirPlantelArea(area)

    input("\nPresione Enter para continuar...")

def interfazReasignacionMasiva():
    clear()
    print("--- Reasignación masiva por año de ingreso ---")
    print("Seleccione el área de investigación a modificar:")


    for i, area in enumerate(areas):
        print(f"{i+1}. {TADai.verNombreAreaInvestigacion(area)}")
    
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
                print(f"{i+1}. {TADai.verNombreAreaInvestigacion(area)}")
        areaDestino = int(input("Opción: ")) - 1

        if areaDestino < 0 or areaDestino >= len(areas) or areaDestino == areaAModificar:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue

    clear()

    anioIngreso = int(input("Ingrese el año de inicio de los investigadores a reasignar: "))

    listadoReasignados = []
    i = 0
    maxLen = TADai.tamanioAreaInvestigacion(areas[areaAModificar])
    while i < maxLen:
        investigadorActual = TADai.recuperarInvestigador(areas[areaAModificar], i)
        if TADi.verFechaIngreso(investigadorActual).year == anioIngreso:
            listadoReasignados.append(investigadorActual)
            TADai.eliminarInvestigador(areas[areaAModificar], investigadorActual)
            TADai.agregarInvestigador(areas[areaDestino], investigadorActual)
            maxLen -= 1
        else:
            i += 1
    
    if len(listadoReasignados) == 0:
        print(f"No se encontraron investigadores con año de ingreso {anioIngreso} en el área de investigación {TADai.verNombreAreaInvestigacion(areas[areaAModificar])}.")
        input("Presione Enter para continuar...")
        return

    print(f"\nInvestigadores reasignados del año {anioIngreso}:")
    for reasignado in listadoReasignados:
        print(f" - {TADi.verNombre(reasignado)} {TADi.verApellido(reasignado)}")
        print(f"   Legajo: {TADi.verNroLegajo(reasignado)}")
        print(f"   Año de ingreso: {TADi.verFechaIngreso(reasignado).year}")
        print(f"   Laboratorio: {TADi.verNroLab(reasignado)}")
        print("------------------------------")

    print("Reasignación masiva completada exitosamente.")
    input("Presione Enter para continuar...")

def interfazVerCola(areaDeInvestigacion):

    clear()

def interfazModificarCola():
    pass

def interfazColaPresupuestos():
    flag = True
    while flag:
        clear()
        
        print("--- Cola para presupuestos anuales ---")
        for i, area in enumerate(areas):
            print(f"{i+1}. {TADai.verNombreAreaInvestigacion(area)}")
        areaSeleccionada = int(input("Seleccione un área de investigación: ")) - 1
        
        clear()

        while True:
            print("1. Ver Cola")
            print("2. Modificar Cola")
            print("3. Volver al menú principal")
            opcion = int(input("Opción: "))
            if opcion == 1:
                interfazVerCola(areaSeleccionada)
            elif opcion == 2:
                interfazModificarCola()
            elif opcion == 3:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")

        print("")

def interfazGrafica():
    while True:
        clear()
        opcion = menuPrincipal()
        
        if opcion == "1":
            interfazAgregarInvestigador()
        elif opcion == "2":
            interfazModificarInvestigador()
        elif opcion == "3":
            intefazBajaPersonal()
        elif opcion == "4":
            intefazMostrarPlantel()
        elif opcion == "5":
            interfazReasignacionMasiva()
        elif opcion == "6":
            interfazColaPresupuestos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
    return

def main():
    interfazGrafica()
    return

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error inesperado: {e}")