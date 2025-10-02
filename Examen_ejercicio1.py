# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 15:00:30 2025

@author: CABLE CENTRO SA
"""

# Importar el módulo os para operaciones del sistema operativo
# Este módulo nos permite verificar si archivos existen en el sistema
import os

# Función principal del programa - actúa como el controlador central
def main():
    """
    Función principal que controla el flujo del programa.
    Contiene el menú principal y dirige a las diferentes funcionalidades.
    """
    # Bucle infinito que mantiene el programa ejecutándose hasta que el usuario elija salir
    # Esto permite que el usuario realice múltiples operaciones sin reiniciar el programa
    while True:
        # Mostrar el menú principal con las opciones disponibles
        # Usamos \n para crear saltos de línea y === para un encabezado visualmente claro
        print("\n" + "="*40)
        print("      SISTEMA DE REGISTRO DE NOTAS")
        print("="*40)
        print("1. Crear archivo nuevo (SOBRESCRIBE EXISTENTE)")
        print("2. Agregar estudiantes al archivo actual")
        print("3. Obtener información del archivo existente")
        print("4. Salir del programa")
        print("-"*40)
        
        # Solicitar al usuario que ingrese su selección
        # input() pausa el programa y espera la entrada del usuario
        opcion = input("Seleccione una opción (1-4): ")
        
        # Estructura condicional para determinar qué acción ejecutar
        # basándose en la opción seleccionada por el usuario
        if opcion == "1":
            # Opción 1: Crear un nuevo archivo (sobrescribe si existe)
            crear_archivo()
        elif opcion == "2":
            # Opción 2: Agregar nuevos estudiantes al archivo existente
            agregar_estudiantes()
        elif opcion == "3":
            # Opción 3: Acceder al submenú de consultas e informes
            menu_informacion()
        elif opcion == "4":
            # Opción 4: Salir del programa - break rompe el bucle while
            print("¡Gracias por usar el sistema! ¡Hasta luego!")
            break
        else:
            # Manejo de opciones inválidas - informar al usuario del error
            print("Opción inválida. Por favor seleccione un número entre 1 y 4.")

# Función para crear un archivo nuevo desde cero
def crear_archivo():
    """
    Crea un nuevo archivo CSV sobrescribiendo cualquier archivo existente con el mismo nombre.
    Incluye los encabezados de columnas y permite agregar estudiantes inmediatamente.
    """
    # Abrir el archivo en modo escritura ("w")
    # - "w" significa write (escritura): crea el archivo si no existe, lo sobrescribe si existe
    # - encoding="utf-8" asegura que se puedan usar caracteres especiales (tildes, ñ, etc.)
    # - with open() cierra automáticamente el archivo al terminar el bloque
    with open("Notas.csv", "w", encoding="utf-8") as archivo:
        # Escribir la línea de encabezados en formato CSV
        # Cada columna separada por comas, terminando con \n (nueva línea)
        archivo.write("Nombre,Primer_apellido,Segundo_apellido,Español,Inglés,Estudios_sociales,Matemáticas,Ciencias\n")
    
    # Mensaje de confirmación para el usuario
    print("Archivo 'Notas.csv' creado exitosamente.")
    print("Los encabezados han sido establecidos:")
    print("   Nombre, Primer_apellido, Segundo_apellido, Español, Inglés, Estudios_sociales, Matemáticas, Ciencias")
    
    # Preguntar si desea agregar estudiantes inmediatamente después de crear el archivo
    # Esto mejora la experiencia de usuario evitando que tenga que volver al menú
    respuesta = input("\n¿Desea agregar estudiantes ahora? (s/n): ")
    if respuesta.lower() == 's':
        agregar_estudiantes()

# Función para agregar nuevos estudiantes al archivo existente
def agregar_estudiantes():
    """
    Permite agregar uno o múltiples estudiantes al archivo CSV existente.
    Si el archivo no existe, ofrece crearlo automáticamente.
    """
    # Verificar si el archivo existe antes de intentar agregar datos
    # os.path.exists() retorna True si el archivo existe, False si no
    if not os.path.exists("Notas.csv"):
        print("El archivo 'Notas.csv' no existe.")
        # Ofrecer crear el archivo automáticamente para mayor comodidad
        crear = input("¿Desea crearlo ahora? (s/n): ")
        if crear.lower() == 's':
            crear_archivo()
        else:
            # Si el usuario no quiere crear el archivo, regresar al menú principal
            print("Regresando al menú principal...")
            return
    
    # Contador para llevar registro de cuántos estudiantes se han agregado en esta sesión
    estudiantes_agregados = 0
    
    # Bucle para permitir agregar múltiples estudiantes sin volver al menú
    while True:
        print("\n" + "-"*50)
        print("        AGREGAR NUEVO ESTUDIANTE")
        print("-"*50)
        
        # Solicitar los datos personales del estudiante
        # input() siempre retorna un string, no necesita conversión
        print("\n Datos personales:")
        nombre = input("   Nombre: ")
        apellido1 = input("   Primer apellido: ")
        apellido2 = input("   Segundo apellido: ")
        
        # Solicitar las notas de cada materia
        # Mostramos instrucciones claras sobre el rango de notas permitido
        print("\n Ingrese las notas (escala de 0 a 100):")
        español = input("   Español: ")
        ingles = input("   Inglés: ")
        estudios_sociales = input("   Estudios sociales: ")
        matematicas = input("   Matemáticas: ")
        ciencias = input("   Ciencias: ")
        
        # Abrir el archivo en modo append ("a")
        # - "a" significa append (añadir): agrega al final del archivo sin borrar contenido existente
        # - encoding="utf-8" mantiene la consistencia con la creación del archivo
        with open("Notas.csv", "a", encoding="utf-8") as archivo:
            # Formatear los datos como una línea CSV
            # f-string permite insertar variables dentro del string
            # \n al final asegura que cada estudiante esté en una línea separada
            linea = f"{nombre},{apellido1},{apellido2},{español},{ingles},{estudios_sociales},{matematicas},{ciencias}\n"
            
            # Escribir la línea formateada en el archivo
            archivo.write(linea)
        
        # Incrementar el contador y mostrar confirmación
        estudiantes_agregados += 1
        print(f"Estudiante '{nombre} {apellido1} {apellido2}' agregado exitosamente.")
        print(f"   Total agregados en esta sesión: {estudiantes_agregados}")
        
        # Preguntar si desea continuar agregando más estudiantes
        # .lower() convierte la respuesta a minúsculas para comparación case-insensitive
        continuar = input("\n¿Desea agregar otro estudiante? (s/n): ")
        if continuar.lower() != 's':
            # Mostrar resumen final antes de salir
            print(f"\n Resumen: Se agregaron {estudiantes_agregados} estudiantes en esta sesión.")
            break

# Función para el submenú de consultas e informes
def menu_informacion():
    """
    Submenú que ofrece diversas opciones para consultar y analizar los datos del archivo.
    Incluye cálculos de promedios, estados de aprobación y búsquedas específicas.
    """
    # Verificar existencia del archivo antes de permitir consultas
    if not os.path.exists("Notas.csv"):
        print(" El archivo 'Notas.csv' no existe.")
        print("   Por favor, cree el archivo primero usando la opción 1 del menú principal.")
        return
    
    # Bucle para el submenú de información
    while True:
        print("\n" + "="*45)
        print("       CONSULTAS E INFORMES")
        print("="*45)
        print("1.  Calcular promedio general del grupo")
        print("2.  Calcular promedio de un estudiante específico")
        print("3.  Listar todos los estudiantes (aprobados/reprobados)")
        print("4.  Buscar estudiante por número de línea")
        print("5.   Volver al menú principal")
        print("-"*45)
        
        # Solicitar opción del submenú
        opcion = input("Seleccione una opción (1-5): ")
        
        # Procesar la selección del submenú
        if opcion == "1":
            promedio_grupo()
        elif opcion == "2":
            promedio_estudiante()
        elif opcion == "3":
            listar_aprobados()
        elif opcion == "4":
            buscar_por_linea()
        elif opcion == "5":
            # break rompe el bucle del submenú y regresa al menú principal
            print("Regresando al menú principal...")
            break
        else:
            print(" Opción inválida. Por favor seleccione un número entre 1 y 5.")

# Función para calcular el promedio general de todo el grupo
def promedio_grupo():
    """
    Calcula y muestra el promedio general de todas las notas de todos los estudiantes.
    Lee todo el archivo, procesa cada estudiante y calcula el promedio global.
    """
    # Abrir y leer todo el contenido del archivo
    # "r" significa read (lectura) - solo para leer, no modificar
    with open("Notas.csv", "r", encoding="utf-8") as archivo:
        # readlines() lee todas las líneas y las retorna como una lista
        # Cada elemento de la lista es una línea del archivo
        lineas = archivo.readlines()
    
    # Verificar que el archivo contenga datos además del encabezado
    # len(lineas) <= 1 significa que solo tiene encabezado o está vacío
    if len(lineas) <= 1:
        print(" El archivo no contiene estudiantes registrados.")
        return
    
    # Variables para acumular los cálculos
    total_promedios = 0.0    # Acumula la suma de todos los promedios individuales
    cantidad_estudiantes = 0 # Cuenta cuántos estudiantes hay
    
    print("\nCalculando promedio del grupo...")
    
    # Procesar cada línea del archivo, empezando desde la línea 1 (omitir encabezado en línea 0)
    # range(1, len(lineas)) crea una secuencia desde 1 hasta el número total de líneas - 1
    for i in range(1, len(lineas)):
        # strip() elimina espacios en blanco al inicio y final (incluyendo \n)
        # split(",") divide la línea en una lista usando comas como separadores
        datos = lineas[i].strip().split(",")
        
        # Las notas están en las posiciones 3 a 7 (índices 3, 4, 5, 6, 7)
        # Convertir cada nota de string a float para poder hacer cálculos matemáticos
        # float() convierte strings a números decimales
        notas = [float(datos[j]) for j in range(3, 8)]
        
        # Calcular el promedio individual del estudiante
        # sum() suma todos los elementos de la lista 'notas'
        # len(notas) retorna la cantidad de notas (siempre 5 en este caso)
        promedio_individual = sum(notas) / len(notas)
        
        # Acumular para el cálculo del promedio general
        total_promedios += promedio_individual
        cantidad_estudiantes += 1
    
    # Calcular el promedio general del grupo
    # Evitar división por cero (aunque ya verificamos que hay estudiantes)
    if cantidad_estudiantes > 0:
        promedio_general = total_promedios / cantidad_estudiantes
        print("\nRESUMEN DE GRUPO:")
        print(f"   • Total de estudiantes: {cantidad_estudiantes}")
        print(f"   • Promedio general del grupo: {promedio_general:.2f}")
        
        # Información adicional sobre el rango del promedio
        if promedio_general >= 90:
            print("   • Nivel: Excelente ")
        elif promedio_general >= 80:
            print("   • Nivel: Muy Bueno ")
        elif promedio_general >= 70:
            print("   • Nivel: Bueno ")
        else:
            print("   • Nivel: Necesita mejora ")
    else:
        print(" No se pudieron procesar los datos.")

# Función para calcular el promedio de un estudiante específico
def promedio_estudiante():
    """
    Busca un estudiante por nombre y apellidos y calcula su promedio individual.
    Permite búsqueda exacta por los tres campos: nombre, primer y segundo apellido.
    """
    print("\n Búsqueda de estudiante")
    print("   (Ingrese los datos exactos como están registrados)")
    
    # Solicitar los datos de identificación del estudiante
    nombre = input("   Nombre: ")
    apellido1 = input("   Primer apellido: ")
    apellido2 = input("   Segundo apellido: ")
    
    # Leer todo el archivo para buscar el estudiante
    with open("Notas.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    # Bandera para indicar si se encontró el estudiante
    estudiante_encontrado = False
    
    print(f"\n Buscando: {nombre} {apellido1} {apellido2}...")
    
    # Buscar en todas las líneas del archivo (omitir encabezado en línea 0)
    for i in range(1, len(lineas)):
        datos = lineas[i].strip().split(",")
        
        # Comparar los datos buscados con los registrados
        # datos[0] = Nombre, datos[1] = Primer apellido, datos[2] = Segundo apellido
        if (datos[0] == nombre and datos[1] == apellido1 and datos[2] == apellido2):
            # Estudiante encontrado - calcular su promedio
            notas = [float(datos[j]) for j in range(3, 8)]
            promedio = sum(notas) / len(notas)
            
            # Mostrar los resultados detallados
            print("\n ESTUDIANTE ENCONTRADO:")
            print(f"   • Nombre completo: {nombre} {apellido1} {apellido2}")
            print("   • Notas individuales:")
            print(f"     - Español: {notas[0]}")
            print(f"     - Inglés: {notas[1]}")
            print(f"     - Estudios Sociales: {notas[2]}")
            print(f"     - Matemáticas: {notas[3]}")
            print(f"     - Ciencias: {notas[4]}")
            print(f"   • Promedio general: {promedio:.2f}")
            
            # Determinar y mostrar el estado de aprobación
            estado = " APROBADO" if promedio >= 70 else " REPROBADO"
            print(f"   • Estado: {estado}")
            
            # Información adicional sobre el rendimiento
            if promedio >= 90:
                print("   • Desempeño: Excelente ")
            elif promedio >= 80:
                print("   • Desempeño: Muy Bueno ")
            elif promedio >= 70:
                print("   • Desempeño: Aceptable ")
            else:
                print("   • Desempeño: Necesita mejorar ")
            
            estudiante_encontrado = True
            break  # Romper el bucle una vez encontrado el estudiante
    
    # Si no se encontró el estudiante después de revisar todo el archivo
    if not estudiante_encontrado:
        print(f" Estudiante '{nombre} {apellido1} {apellido2}' no encontrado.")
        print("   Verifique que los datos estén escritos exactamente igual que en el registro.")

# Función para listar todos los estudiantes con su estado de aprobación
def listar_aprobados():
    """
    Lista todos los estudiantes mostrando su nombre completo y estado de aprobación.
    Calcula el promedio de cada estudiante y determina si aprueba (≥70) o reprueba.
    """
    # Leer todo el contenido del archivo
    with open("Notas.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    # Verificar que haya datos para procesar
    if len(lineas) <= 1:
        print(" El archivo no contiene estudiantes registrados.")
        return
    
    print("\n" + "="*60)
    print("              ESTADO ACADÉMICO DE ESTUDIANTES")
    print("="*60)
    print(" APROBADO (≥70) | REPROBADO (<70)")
    print("-"*60)
    
    # Contadores para estadísticas
    total_aprobados = 0
    total_reprobados = 0
    
    # Procesar cada estudiante en el archivo
    for i in range(1, len(lineas)):
        datos = lineas[i].strip().split(",")
        
        # Calcular el promedio del estudiante actual
        notas = [float(datos[j]) for j in range(3, 8)]
        promedio = sum(notas) / len(notas)
        
        # Determinar el estado y el emoji/indicador visual
        if promedio >= 70:
            estado = " APROBADO"
            total_aprobados += 1
        else:
            estado = " REPROBADO"
            total_reprobados += 1
        
        # Mostrar la información formateada del estudiante
        # :<15 alinea el texto a la izquierda con 15 caracteres de espacio
        nombre_completo = f"{datos[0]} {datos[1]} {datos[2]}"
        print(f" {estado} | {nombre_completo:<30} | Promedio: {promedio:6.2f}")
    
    # Mostrar resumen estadístico al final
    print("-"*60)
    total_estudiantes = total_aprobados + total_reprobados
    if total_estudiantes > 0:
        porcentaje_aprobados = (total_aprobados / total_estudiantes) * 100
        print(" RESUMEN ESTADÍSTICO:")
        print(f"   • Total de estudiantes: {total_estudiantes}")
        print(f"   • Aprobados: {total_aprobados} ({porcentaje_aprobados:.1f}%)")
        print(f"   • Reprobados: {total_reprobados} ({100 - porcentaje_aprobados:.1f}%)")

# Función para buscar un estudiante por su número de línea en el archivo
def buscar_por_linea():
    """
    Permite acceder directamente a un estudiante específico usando su número de línea.
    Útil para cuando se conoce la posición del estudiante en la lista.
    """
    # Leer todo el archivo para conocer la cantidad de estudiantes
    with open("Notas.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    # Calcular cuántos estudiantes hay (total de líneas - 1 por el encabezado)
    cantidad_estudiantes = len(lineas) - 1
    
    # Mostrar información sobre la cantidad disponible
    print(f"\n El archivo contiene {cantidad_estudiantes} estudiantes registrados.")
    print(f"   Los números de línea válidos son del 1 al {cantidad_estudiantes}.")
    
    # Validar que haya estudiantes para buscar
    if cantidad_estudiantes == 0:
        print(" No hay estudiantes registrados para buscar.")
        return
    
    # Solicitar el número de línea con manejo de errores
    try:
        # int() convierte el string input a número entero
        numero = int(input("\nIngrese el número de línea a buscar: "))
    except ValueError:
        # ValueError ocurre si el usuario ingresa algo que no se puede convertir a número
        print(" Error: Debe ingresar un número entero válido.")
        return
    
    # Validar que el número esté dentro del rango permitido
    if numero < 1 or numero > cantidad_estudiantes:
        print(f" Número inválido. Debe estar entre 1 y {cantidad_estudiantes}.")
        return
    
    # Obtener los datos del estudiante en la línea solicitada
    # +1 porque las listas empiezan en 0, pero mostramos al usuario desde 1
    datos = lineas[numero].strip().split(",")
    
    # Calcular el promedio del estudiante
    notas = [float(datos[j]) for j in range(3, 8)]
    promedio = sum(notas) / len(notas)
    
    # Mostrar la información del estudiante encontrado
    print(f"\n ESTUDIANTE EN LÍNEA {numero}:")
    print(f"   • Nombre completo: {datos[0]} {datos[1]} {datos[2]}")
    print("   • Notas por materia:")
    print(f"     - Español: {notas[0]}")
    print(f"     - Inglés: {notas[1]}")
    print(f"     - Estudios Sociales: {notas[2]}")
    print(f"     - Matemáticas: {notas[3]}")
    print(f"     - Ciencias: {notas[4]}")
    print(f"   • Promedio general: {promedio:.2f}")
    
    # Estado de aprobación
    estado = " APROBADO" if promedio >= 70 else "REPROBADO"
    print(f"   • Estado: {estado}")

# Punto de entrada principal del programa
# Esta condición verifica si el script se está ejecutando directamente
# (no importado como módulo)
if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Se ejecuta solo cuando el archivo se ejecuta directamente.
    """
    print(" Iniciando Sistema de Registro de Notas...")
    print("   Desarrollado para: Colegio Científico de San Vito")
    print("   Asignatura: Programación en Python - Undécimo nivel")
    main()  # Llamar a la función principal para iniciar el programa