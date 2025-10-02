# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 19:26:30 2025

@author: CABLE CENTRO SA
"""

# Importar módulos necesarios para el juego
import random  # Para selección aleatoria y desordenar palabras
      

# Función principal del juego Scramble
def main_scramble():
    """
    Función principal que controla todo el juego Scramble.
    Gestiona el menú principal, las partidas y el resumen de resultados.
    """
    print(" BIENVENIDO AL JUEGO SCRAMBLE ")
    print("=" * 50)
    print("Adivina la palabra correcta a partir de las letras desordenadas!")
    print("=" * 50)
    
    # Cargar la lista de palabras desde el archivo CSV
    # Esto se hace una vez al inicio del juego
    lista_palabras = cargar_palabras_desde_archivo()
    
    # Si no se pudieron cargar las palabras, terminar el juego
    if not lista_palabras:
        print(" Error: No se pudieron cargar las palabras del archivo.")
        return
    
    # Variables para llevar el registro del juego
    partidas_ganadas = 0           # Contador de partidas ganadas
    partidas_totales = 0           # Contador de partidas jugadas
    palabras_acertadas = []        # Lista de palabras que el usuario acertó
    palabras_falladas = []         # Lista de palabras que el usuario falló
    
    # Solicitar al usuario la cantidad de oportunidades por partida
    # Con manejo de errores para entradas inválidas
    while True:
        try:
            oportunidades = int(input("\n¿Con cuántas oportunidades deseas jugar? (ej: 3, 5, 10): "))
            if oportunidades > 0:
                break
            else:
                print(" Por favor ingresa un número mayor a 0.")
        except ValueError:
            print(" Error: Debes ingresar un número entero válido.")
    
    print(f"\n Configuración lista: {oportunidades} oportunidades por partida")
    
    # Bucle principal del juego - permite múltiples partidas
    while True:
        # Jugar una partida individual
        resultado = jugar_partida(lista_palabras, oportunidades)
        
        # Actualizar estadísticas basadas en el resultado de la partida
        partidas_totales += 1
        if resultado["acierto"]:
            partidas_ganadas += 1
            palabras_acertadas.append(resultado["palabra_correcta"])
            print(f"\n ¡CORRECTO! Ganaste 1 punto. Puntos totales: {partidas_ganadas}")
        else:
            palabras_falladas.append(resultado["palabra_correcta"])
            print(f"\n¡Fallaste! La palabra era: {resultado['palabra_correcta']}")
        
        # Guardar el resultado en el archivo
        guardar_resultado(resultado)
        
        # Mostrar menú después de cada partida
        opcion = menu_after_game()
        
        # Procesar la opción seleccionada por el usuario
        if opcion == "1":
            # Verificar si aún hay palabras disponibles
            if len(lista_palabras) == 0:
                print("\n ¡FELICIDADES! Has agotado todas las palabras disponibles.")
                print("   No hay más palabras para jugar.")
                break
            else:
                print(f"\n Iniciando nueva partida... Palabras restantes: {len(lista_palabras)}")
                continue
        elif opcion == "2":
            # Mostrar resumen de estadísticas
            mostrar_resumen(partidas_ganadas, partidas_totales, palabras_acertadas, palabras_falladas)
            
            # Preguntar si quiere seguir jugando después de ver el resumen
            continuar = input("\n¿Deseas seguir jugando? (s/n): ").lower()
            if continuar != 's':
                break
        elif opcion == "3":
            # Salir del juego
            break
    
    # Mostrar resumen final al terminar el juego
    print("\n" + "=" * 50)
    print("           RESUMEN FINAL DEL JUEGO")
    print("=" * 50)
    mostrar_resumen(partidas_ganadas, partidas_totales, palabras_acertadas, palabras_falladas)
    print("\n¡Gracias por jugar Scramble! ")

def cargar_palabras_desde_archivo():
    """
    Carga las palabras desde el archivo CSV y selecciona 200 aleatorias.
    
    Returns:
        list: Lista de 200 palabras seleccionadas aleatoriamente, o todas las disponibles si hay menos de 200.
    """
    try:
        # Intentar abrir el archivo de palabras
        # 'r' modo lectura, 'utf-8' encoding para caracteres especiales
        with open("words (1).csv", "r", encoding="utf-8") as archivo:
            # Leer todo el contenido del archivo
            contenido = archivo.read().strip()  # strip() elimina espacios en blanco al inicio y final
            
        # Dividir el contenido usando punto y coma como separador
        # El archivo tiene todas las palabras en una línea separadas por ;
        todas_las_palabras = contenido.split(";")
        
        # Filtrar palabras vacías (por si hay separadores dobles)
        todas_las_palabras = [palabra for palabra in todas_las_palabras if palabra.strip()]
        
        print(f" Se cargaron {len(todas_las_palabras)} palabras del archivo.")
        
        # Seleccionar 200 palabras aleatorias, o todas si hay menos de 200
        if len(todas_las_palabras) > 200:
            # random.sample() selecciona 200 elementos únicos sin repetición
            palabras_seleccionadas = random.sample(todas_las_palabras, 200)
            print(" Se seleccionaron 200 palabras aleatorias para el juego.")
        else:
            # Si hay menos de 200 palabras, usar todas las disponibles
            palabras_seleccionadas = todas_las_palabras
            print(f"Se usarán todas las {len(palabras_seleccionadas)} palabras disponibles.")
        
        return palabras_seleccionadas
        
    except FileNotFoundError:
        # Manejar el caso en que el archivo no existe
        print(" Error: El archivo 'words (1).csv' no se encuentra.")
        print("   Asegúrate de que el archivo esté en la misma carpeta que el programa.")
        return []
    except Exception as e:
        # Manejar cualquier otro error inesperado
        print(f" Error inesperado al cargar el archivo: {e}")
        return []

def jugar_partida(lista_palabras, oportunidades_iniciales):
    """
    Ejecuta una partida individual del juego Scramble.
    
    Args:
        lista_palabras (list): Lista de palabras disponibles para jugar
        oportunidades_iniciales (int): Número de oportunidades para adivinar
    
    Returns:
        dict: Diccionario con los resultados de la partida
    """
    # Verificar que aún hay palabras disponibles
    if len(lista_palabras) == 0:
        print(" No hay más palabras disponibles para jugar.")
        return {"acierto": False, "palabra_correcta": "", "oportunidades_usadas": 0}
    
    # Seleccionar una palabra aleatoria de la lista
    palabra_correcta = random.choice(lista_palabras)
    
    # Eliminar la palabra seleccionada de la lista para no repetirla
    lista_palabras.remove(palabra_correcta)
    
    # Desordenar la palabra usando random.sample()
    # random.sample(palabra, len(palabra)) devuelve una lista de letras desordenadas
    # "".join() une las letras en un string
    palabra_desordenada = "".join(random.sample(palabra_correcta, len(palabra_correcta)))
    
    # Inicializar variables para la partida actual
    oportunidades_restantes = oportunidades_iniciales
    acierto = False
    oportunidades_usadas = 0
    
    print(f"\n{'=' * 60}")
    print("              NUEVA PARTIDA")
    print(f"{'=' * 60}")
    print(f"Palabra desordenada: {palabra_desordenada}")
    print(f" Pista: La palabra tiene {len(palabra_correcta)} letras")
    print(f"Oportunidades restantes: {oportunidades_restantes}")
    print(f"{'-' * 60}")
    
    # Bucle para los intentos de adivinanza
    while oportunidades_restantes > 0 and not acierto:
        # Solicitar intento al usuario
        intento = input("¿Cuál crees que es la palabra correcta? : ").strip().lower()
        oportunidades_usadas += 1
        
        # Verificar si el intento es correcto (case-insensitive)
        if intento == palabra_correcta.lower():
            acierto = True
        else:
            # Restar una oportunidad por intento fallido
            oportunidades_restantes -= 1
            
            # Mostrar mensaje según las oportunidades restantes
            if oportunidades_restantes > 0:
                print(f"Incorrecto. Oportunidades restantes: {oportunidades_restantes}")
                
                # Dar pista después del primer error si la palabra es larga
                if len(palabra_correcta) >= 6 and oportunidades_restantes == oportunidades_iniciales - 1:
                    print(f" Pista: La palabra empieza con '{palabra_correcta[0]}'")
            else:
                print(" ¡Se te acabaron las oportunidades!")
    
    # Retornar los resultados de la partida
    return {
        "acierto": acierto,
        "palabra_correcta": palabra_correcta,
        "oportunidades_usadas": oportunidades_usadas,
        "oportunidades_totales": oportunidades_iniciales
    }

def guardar_resultado(resultado):
    """
    Guarda el resultado de cada partida en el archivo 'Resultados.txt'
    
    Args:
        resultado (dict): Diccionario con la información del resultado de la partida
    """
    # Determinar el nombre del archivo donde guardar los resultados
    archivo_resultados = "Resultados.txt"
    
    # Abrir el archivo en modo append ('a') para agregar sin borrar contenido anterior
    with open(archivo_resultados, "a", encoding="utf-8") as archivo:
        # Formatear la línea de resultado
        if resultado["acierto"]:
            estado = "ACERTÓ"
            puntaje = "+1 punto"
        else:
            estado = "FALLÓ"
            puntaje = "0 puntos"
        
        # Crear línea con formato: Palabra | Estado | Oportunidades usadas/totales | Puntaje
        linea = f"Palabra: {resultado['palabra_correcta']} | {estado} | Oportunidades: {resultado['oportunidades_usadas']}/{resultado['oportunidades_totales']} | {puntaje}\n"
        
        # Escribir la línea en el archivo
        archivo.write(linea)
    
    # Mensaje de confirmación (opcional, para debugging)
    # print(f" Resultado guardado en {archivo_resultados}")

def menu_after_game():
    """
    Muestra el menú después de cada partida y valida la entrada del usuario.
    
    Returns:
        str: Opción seleccionada por el usuario ('1', '2', o '3')
    """
    # Bucle hasta que se ingrese una opción válida
    while True:
        print("\n" + "=" * 50)
        print("           ¿QUÉ DESEAS HACER AHORA?")
        print("=" * 50)
        print("1.  Jugar otra partida")
        print("2.  Obtener resumen hasta el momento")
        print("3. Salir del juego")
        print("-" * 50)
        
        # Solicitar opción al usuario
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        # Validar que la opción sea válida
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print(" Opción inválida. Por favor selecciona 1, 2 o 3.")

def mostrar_resumen(ganadas, totales, acertadas, falladas):
    """
    Muestra un resumen detallado de las estadísticas del juego.
    
    Args:
        ganadas (int): Número de partidas ganadas
        totales (int): Número total de partidas jugadas
        acertadas (list): Lista de palabras acertadas
        falladas (list): Lista de palabras falladas
    """
    print("\n" + "=" * 60)
    print("                RESUMEN DE ESTADÍSTICAS")
    print("=" * 60)
    
    # Calcular porcentajes (evitando división por cero)
    if totales > 0:
        porcentaje_ganadas = (ganadas / totales) * 100
        porcentaje_perdidas = 100 - porcentaje_ganadas
    else:
        porcentaje_ganadas = porcentaje_perdidas = 0
    
    # Mostrar estadísticas generales
    print(" ESTADÍSTICAS GENERALES:")
    print(f"   • Partidas jugadas: {totales}")
    print(f"   • Partidas ganadas: {ganadas} ({porcentaje_ganadas:.1f}%)")
    print(f"   • Partidas perdidas: {totales - ganadas} ({porcentaje_perdidas:.1f}%)")
    print(f"   • Puntuación total: {ganadas} puntos")
    
    # Mostrar palabras acertadas
    print(f"\n PALABRAS ACERTADAS ({len(acertadas)}):")
    if acertadas:
        # Mostrar hasta 10 palabras acertadas, si hay más mostrar "..."
        for i, palabra in enumerate(acertadas[:10]):
            print(f"   {i+1}. {palabra}")
        if len(acertadas) > 10:
            print(f"   ... y {len(acertadas) - 10} más")
    else:
        print("   (No hay palabras acertadas todavía)")
    
    # Mostrar palabras falladas
    print(f"\n PALABRAS FALLADAS ({len(falladas)}):")
    if falladas:
        # Mostrar hasta 10 palabras falladas, si hay más mostrar "..."
        for i, palabra in enumerate(falladas[:10]):
            print(f"   {i+1}. {palabra}")
        if len(falladas) > 10:
            print(f"   ... y {len(falladas) - 10} más")
    else:
        print("   (No hay palabras falladas)")
    
    # Mostrar evaluación del desempeño
    print("\n EVALUACIÓN:")
    if totales > 0:
        if porcentaje_ganadas >= 80:
            print("   ¡Excelente! Eres un maestro del Scramble! ")
        elif porcentaje_ganadas >= 60:
            print("   Muy buen trabajo! Sigue así! ")
        elif porcentaje_ganadas >= 40:
            print("   Buen desempeño! Puedes mejorar! ")
        else:
            print("   Sigue practicando! Mejorarás con el tiempo! ")
    else:
        print("   Aún no hay suficientes datos para evaluación.")

# Punto de entrada del programa Scramble
if __name__ == "__main__":
    """
    Punto de entrada principal del juego Scramble.
    Se ejecuta cuando este archivo se ejecuta directamente.
    """
    # Llamar a la función principal del juego
    main_scramble()