import os
from datetime import date
from random import randint

import TADareaInvestigacion as TADai
import TADcola
import TADInvestigador as TADi

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


def cargaInicial(cantidad=20):
    nombres = [
        "Juan",
        "María",
        "Carlos",
        "Ana",
        "Luis",
        "Sofía",
        "Miguel",
        "Lucía",
        "Diego",
        "Valentina",
        "Santiago",
        "Manuel",
        "Thomas",
        "Ezequiel",
    ]
    apellidos = [
        "García",
        "Rodríguez",
        "López",
        "Martínez",
        "Pérez",
        "Gómez",
        "Sánchez",
        "Díaz",
        "Fernández",
        "Torres",
        "Silva",
        "Talone",
        "Linares",
        "Barrios",
    ]
    for i in range(cantidad):
        nombre = nombres[randint(0, len(nombres) - 1)]
        apellido = apellidos[randint(0, len(apellidos) - 1)]
        legajo = randint(30000, 39999)
        while buscarInvestigadorPorLegajo(legajo) is not None:
            legajo = randint(30000, 39999)
        anioIngreso = randint(1980, 2025)
        mesIngreso = randint(1, 12)
        if mesIngreso == 2:
            diaIngreso = randint(1, 28)
        elif mesIngreso in [4, 6, 9, 11]:
            diaIngreso = randint(1, 30)
        else:
            diaIngreso = randint(1, 31)
        fechaIngreso = date(anioIngreso, mesIngreso, diaIngreso)
        nroLaboratorio = randint(1, 10)

        nuevoInvestigador = TADi.crearInvestigador()
        TADi.cargarInvestigador(
            nuevoInvestigador, nombre, apellido, legajo, fechaIngreso, nroLaboratorio
        )

        areaSeleccionada = areas[randint(0, len(areas) - 1)]
        TADai.agregarInvestigador(areaSeleccionada, nuevoInvestigador)


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
                print(f"{i + 1}. {TADai.verNombreAreaInvestigacion(area)}")
            print("0. Volver al menú principal")
            areaSeleccionada = int(input("Opción: ")) - 1
            if areaSeleccionada == -1:
                break
            if areaSeleccionada < 0 or areaSeleccionada >= len(areas):
                raise ValueError("Indice de área no válido. Intente nuevamente.")

            legajo = int(input("Ingrese el legajo: "))
            if legajo <= 0:
                raise ValueError("El legajo tiene que mayor a 0.")
            if buscarInvestigadorPorLegajo(legajo) is not None:
                raise ValueError(
                    "El legajo ingresado ya existe. Intente con otro legajo."
                )
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
        TADi.cargarInvestigador(
            nuevoInvestigador, nombre, apellido, legajo, fechaIngreso, nroLaboratorio
        )

        TADai.agregarInvestigador(areas[areaSeleccionada], nuevoInvestigador)
        print()
        imprimirInvestigador(nuevoInvestigador, primeraLinea=True)
        print()

        print("Investigador agregado exitosamente.")
        continuar = input("¿Desea agregar otro investigador? (s/n): ")
        if continuar.lower() != "s":
            flag = False


def interfazModificarInvestigador():
    flag = True
    while flag:
        clear()
        print("--- Modificar Investigadores ---")
        print("Investigadores disponibles:")
        for area in areas:
            print(f"\nÁrea de Investigación: {TADai.verNombreAreaInvestigacion(area)}")
            for j in range(TADai.tamanioAreaInvestigacion(area)):
                investigador = TADai.recuperarInvestigador(area, j)
                print(
                    f" - {TADi.verNombre(investigador)} {TADi.verApellido(investigador)} (Legajo: {TADi.verNroLegajo(investigador)})"
                )
        print(
            "Ingrese el legajo del investigador a modificar (ingrese 0 para volver al menú principal):"
        )
        try:
            legajo = int(input("Legajo: "))
            if legajo == 0:
                break
            investigador = buscarInvestigadorPorLegajo(legajo)
            if investigador is None:
                raise ValueError("Investigador no encontrado.")
            investigadorOriginal = TADi.crearInvestigador()
            TADi.asignarInvestigador(investigador, investigadorOriginal)
        except ValueError as ve:
            print(f"Opción no válida. Intente nuevamente. {ve}")
            input("Presione Enter para continuar...")
            continue

        while True:
            clear()
            print("--- Modificar Investigadores ---")

            print(
                f"¿Qué dato desea modificar del investigador {TADi.verNombre(investigador)} {TADi.verApellido(investigador)}?"
            )
            print("1. Nombre")
            print("2. Apellido")
            print("3. Fecha de ingreso")
            print("4. Laboratorio")
            try:
                opcion = int(input("Opción: "))

                if opcion == 1:
                    nombre = input("Ingrese el nombre del investigador: ")
                    TADi.modificarNombre(investigador, nombre)
                elif opcion == 2:
                    apellido = input("Ingrese el apellido del investigador: ")
                    TADi.modificarApellido(investigador, apellido)

                elif opcion == 3:
                    # TODO: Cambiar por dd/mm/yyyy
                    # date.fromisoformat()
                    anioIngreso = int(input("Ingrese el año de ingreso: "))
                    mesIngreso = int(input("Ingrese el mes de ingreso: "))
                    diaIngreso = int(input("Ingrese el día de ingreso: "))
                    fechaIngreso = date(anioIngreso, mesIngreso, diaIngreso)
                    TADi.modificarFechaIngreso(investigador, fechaIngreso)

                elif opcion == 4:
                    nroLaboratorio = int(input("Ingrese el n° de laboratorio: "))
                    TADi.modificarNroLab(investigador, nroLaboratorio)

                else:
                    print("Opción no válida. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    continue

            except ValueError as ve:
                print(f"Entrada no válida. Intente nuevamente. {ve}")
                input("Presione Enter para continuar...")
                continue
            except Exception as e:
                print(f"Error: {e}. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue

            continuar = input(
                "¿Desea modificar otro dato del mismo investigador? (s/n): "
            )
            if continuar.lower() != "s":
                break

        print("Investigador modificado exitosamente.")
        print("Anteriormente:")
        print(f" - Nombre: {TADi.verNombre(investigadorOriginal)}")
        print(f" - Apellido: {TADi.verApellido(investigadorOriginal)}")
        print(f" - Fecha de ingreso: {TADi.verFechaIngreso(investigadorOriginal)}")
        print(f" - Laboratorio: {TADi.verNroLab(investigadorOriginal)}")
        print("Ahora:")
        print(f" - Nombre: {TADi.verNombre(investigador)}")
        print(f" - Apellido: {TADi.verApellido(investigador)}")
        print(f" - Fecha de ingreso: {TADi.verFechaIngreso(investigador)}")
        print(f" - Laboratorio: {TADi.verNroLab(investigador)}")
        continuar = input("¿Desea modificar otro investigador? (s/n): ")
        if continuar.lower() != "s":
            flag = False


def interfazBajaPersonal():
    flag = True
    while flag:
        clear()
        # intefazMostrarPlantel()
        print("--- Eliminar Investigadores ---")
        print("Investigadores disponibles:")
        for area in areas:
            print(f"\nÁrea de Investigación: {TADai.verNombreAreaInvestigacion(area)}")
            for j in range(TADai.tamanioAreaInvestigacion(area)):
                investigador = TADai.recuperarInvestigador(area, j)
                print(
                    f" - {TADi.verNombre(investigador)} {TADi.verApellido(investigador)} (Legajo: {TADi.verNroLegajo(investigador)})"
                )
        print(
            "Ingrese el legajo del investigador a eliminar (ingrese 0 para volver al menú principal):"
        )
        try:
            legajo = int(input("Legajo: "))
            if legajo == 0:
                break
            investigador = buscarInvestigadorPorLegajo(legajo)
            if investigador is None:
                raise ValueError("Investigador no encontrado.")
        except ValueError as ve:
            print(f"Opción no válida. Intente nuevamente. {ve}")
            input("Presione Enter para continuar...")
            continue


        encontrado = False
        for area in areas:
            i = 0
            maxLen = TADai.tamanioAreaInvestigacion(area)
            while i < maxLen:
                investigadorActual = TADai.recuperarInvestigador(area, i)
                if TADi.verNroLegajo(investigadorActual) == legajo:
                    imprimirInvestigador(investigadorActual)
                    confirmar = input("¿Desea eliminar al investigador? (s/n): ")
                    if confirmar.lower() == "s":
                        TADai.eliminarInvestigador(area, investigadorActual)
                        print(f"Investigador {TADi.verNombre(investigadorActual)} {TADi.verApellido(investigadorActual)} eliminado exitosamente. \n")
                    encontrado = True
                    break
                i += 1
            if encontrado:
                break
        if not encontrado:
            print("Investigador no encontrado.")

        continuar = input("¿Desea eliminar otro investigador? (s/n): ")
        if continuar.lower() != "s":
            flag = False


def imprimirInvestigador(investigador, primeraLinea=False, indice=None):
    if primeraLinea:
        print(
            f"{"":<3} {'Nombre y apellido':<25} {'Legajo':<10} {'Año de ingreso':<15} {'Laboratorio':<10}"
        )
    nombre = TADi.verNombre(investigador) + " " + TADi.verApellido(investigador)
    legajo = TADi.verNroLegajo(investigador)
    fechaDeIngreso = f"{TADi.verFechaIngreso(investigador).day}/{TADi.verFechaIngreso(investigador).month}/{TADi.verFechaIngreso(investigador).year}"
    nroLaboratorio = TADi.verNroLab(investigador)
    print(
        f"{"" if not indice else indice:<3} {nombre:<25} {legajo:<10} {fechaDeIngreso:<15} {nroLaboratorio:<10}"
    )


def imprimirPlantelArea(area):
    print(f"\nÁrea de Investigación: {TADai.verNombreAreaInvestigacion(area)}")
    if TADai.tamanioAreaInvestigacion(area) == 0:
        print("No hay investigadores en esta área.")
        return
    for j in range(TADai.tamanioAreaInvestigacion(area)):
        investigador = TADai.recuperarInvestigador(area, j)
        imprimirInvestigador(investigador, indice=j + 1, primeraLinea=(j == 0))


def interfazMostrarPlantel():
    clear()
    print("--- Plantel de Investigadores ---")

    for area in areas:
        imprimirPlantelArea(area)

    input("\nPresione Enter para continuar...")


def interfazReasignacionMasiva():
    areaAModificar, areaDestino = None, None
    while True:
        clear()
        print("--- Reasignación masiva por año de ingreso ---")
        print("Seleccione el área de investigación a modificar:")
        try:
            for i, area in enumerate(areas):
                print(f"{i + 1}. {TADai.verNombreAreaInvestigacion(area)}")
            print("0. Volver al menú principal")
            areaAModificar = int(input("Opción: ")) - 1
            if areaAModificar == -1:
                return
            if areaAModificar < 0 or areaAModificar >= len(areas):
                raise ValueError("Indice de área no válido. Intente nuevamente.")

            clear()

            print("Seleccione el área de investigación destino:")
            for i, area in enumerate(areas):
                if i != areaAModificar:
                    print(f"{i + 1}. {TADai.verNombreAreaInvestigacion(area)}")
            areaDestino = int(input("Opción: ")) - 1
            if (
                areaDestino < 0
                or areaDestino >= len(areas)
                or areaDestino == areaAModificar
            ):
                raise ValueError("Indice de área no válido. Intente nuevamente.")

            clear()

            anioIngreso = int(
                input("Ingrese el año de inicio de los investigadores a reasignar: ")
            )

        except ValueError as ve:
            print(f"Opción no válida. Intente nuevamente. {ve}")
            input("Presione Enter para continuar...")
            continue
        except Exception as e:
            print(f"Error: {e}. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        break
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
        print(
            f"No se encontraron investigadores con año de ingreso {anioIngreso} en el área de investigación {TADai.verNombreAreaInvestigacion(areas[areaAModificar])}."
        )
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


def interfazColaPresupuestos():
    while True:
        clear()
        try:
            print("--- Cola para presupuestos anuales ---")
            for i, area in enumerate(areas):
                print(f"{i + 1}. {TADai.verNombreAreaInvestigacion(area)}")
            print("0. Volver al menú principal")
            areaSeleccionada = int(input("Opcion: ")) - 1
            if areaSeleccionada == -1:
                return
            if areaSeleccionada < 0 or areaSeleccionada >= len(areas):
                raise ValueError("Indice de área no válido. Intente nuevamente.")

        except ValueError as ve:
            print(f"Opción no válida. Intente nuevamente. {ve}")
            input("Presione Enter para continuar...")
            continue
        except Exception as e:
            print(f"Error: {e}. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        break

    clear()

    colaPresupuestos = TADcola.crearCola()
    print("--- Cola para presupuestos anuales ---")
    i = 0
    while i < TADai.tamanioAreaInvestigacion(areas[areaSeleccionada]):
        investigadorActual = TADai.recuperarInvestigador(areas[areaSeleccionada], i)
        TADcola.encolar(colaPresupuestos, investigadorActual)
        i += 1

    while not TADcola.colaVacia(colaPresupuestos):
        investigadorActual = TADcola.desencolar(colaPresupuestos)
        print(
            f"Investigador {TADi.verNombre(investigadorActual)} {TADi.verApellido(investigadorActual)} fue desencolado "
        )
    input("Presione Enter para continuar...")


def eliminarPorAntiguedad():
    clear()
    print("--- Eliminar investigadores por antigüedad ---")
    fechaActual = date.today()
    eliminados = []
    for area in areas:
        contadorElimnadorPorArea = 0
        i = 0
        maxLen = TADai.tamanioAreaInvestigacion(area)
        print(f"\nArea de investigación: {TADai.verNombreAreaInvestigacion(area)}")
        while i < maxLen:
            investigadorActual = TADai.recuperarInvestigador(area, i)

            fechaIngreso = TADi.verFechaIngreso(investigadorActual)
            diferenciaFecha = fechaActual - fechaIngreso
            aniosDiferencia = diferenciaFecha.days / 365
            if aniosDiferencia >= 30:
                nombreInvestigador = TADi.verNombre(investigadorActual)
                apellidoInvestigador = TADi.verApellido(investigadorActual)

                print(
                    f"Investigador {nombreInvestigador} {apellidoInvestigador} eliminado por antigüedad"
                )
                eliminados.append([investigadorActual, area])
                contadorElimnadorPorArea += 1
                i += 1
            else:
                i += 1
        if contadorElimnadorPorArea == 0:
            print("No se encontraron investigadores con más de 30 años de antigüedad.") 
    if len(eliminados) == 0:
        input("\nPresione Enter para continuar...")
        return
    respuesta = input(
        f"¿Está seguro que desea eliminar a estos {len(eliminados)} investigadores? (s/n): "
    )
    if respuesta.lower() == "s":
        for investigador, area in eliminados:
            TADai.eliminarInvestigador(area, investigador)
        print(f"\nSe eliminaron {len(eliminados)} investigadores.\n")
    input("Presione Enter para continuar...")


def menuPrincipal():
    print("\n--- Menú Principal ---")
    print("1. Agregar investigador")
    print("2. Modificar investigador")
    print("3. Baja de personal")
    print("4. Mostrar plantel de investigadores")
    print("5. Reasignación masiva por año de ingreso")
    print("6. Cola para presupuestos anuales")
    print("7. Eliminar investigadores por antigüedad")
    print("0. Salir")
    return input("Seleccione una opción: ")


def interfazGrafica():
    while True:
        clear() 
        opcion = menuPrincipal()

        if opcion == "1":
            interfazAgregarInvestigador()
        elif opcion == "2":
            interfazModificarInvestigador()
        elif opcion == "3":
            interfazBajaPersonal()
        elif opcion == "4":
            interfazMostrarPlantel()
        elif opcion == "5":
            interfazReasignacionMasiva()
        elif opcion == "6":
            interfazColaPresupuestos()
        elif opcion == "7":
            eliminarPorAntiguedad()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
    return


def main():
    cargaInicial(10)
    interfazGrafica()
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error inesperado: {e}")
