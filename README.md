# Trabajo Práctico Integrador Sintaxis y Semantica del Lenguaje

### Propuesta de Enunciado: Sistema de Gestión de Investigadores (Centro de CyT)
**Consigna**: Desarrollar una aplicación que permita gestionar la información de los Investigadores y sus laboratorios en un centro de ciencia y tecnología, utilizando los
*Tipos Abstractos de Datos* (TADs) adecuados. \
De cada investigador se registran:
Nombre, Apellido, Legajo (ID único), Fecha de Ingreso al Centro, Número de
Laboratorio y Área de Investigación (ej: Biotecnología, IA, Energías Renovables). El
sistema debe ofrecer un menú interactivo con las siguientes operaciones:

1. **Alta y Modificación de Investigadores**:
Implementar funciones para agregar nuevos investigadores con todos sus datos, así
como modificar la información de un profesional existente (nombre, área de
investigación, laboratorio, etc.) utilizando su legajo.
2. **Baja de Personal**:
Permitir eliminar investigadores del sistema utilizando su Legajo como identificador
único, asegurando que la estructura de datos mantenga su integridad tras la eliminación.
3. **Visualización del Plantel Científico**:
Generar y mostrar un listado con todos los investigadores registrados, incluyendo la
totalidad de sus datos personales y profesionales de manera ordenada.
4. **Reasignación Masiva de Área por Año de Ingreso**:
Permitir cambiar el Área de Investigación de todos los científicos que ingresaron en un
año determinado, facilitando la reorganización de los equipos de trabajo según los
nuevos objetivos del centro.
5. **Depuración por Jubilación (Antigüedad)**:
Eliminar automáticamente del sistema a los investigadores cuya antigüedad en la
institución supere los 30 años, calculada a partir de su fecha de ingreso hasta la
actualidad.

6. **Generación de Cola por Área de Investigación**:
Generar una nueva Cola con los investigadores pertenecientes a un Área de
Investigación específica ingresada por el usuario. Esta cola representa el orden de
prioridad para la asignación de presupuestos anuales y debe mostrarse automáticamente
en pantalla.

### Integrantes

* Talone Santiag
* Barrios Ezequiel
* Silva Manuel
* Linares Thomas
