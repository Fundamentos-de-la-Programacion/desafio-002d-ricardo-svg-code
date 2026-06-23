import random
# ============================================================
# DESAFIO EN CLASES - Juego de Trivia por rondas con ranking
# FPY1101 - Fundamentos de Programacion
# PLANTILLA PARA EL ALUMNO
# ============================================================
#
# Completa las funciones marcadas con # TODO.
# Los comentarios "# INVESTIGA:" te dicen QUE buscar (no como hacerlo).
# El programa NO funcionara hasta que completes la logica.
# ============================================================

# INVESTIGA (1): el modulo random para elegir preguntas al azar.
#   Busca: "python modulo random", "python random sample".
#   Escribe aqui el import que necesitas para usar random.
# import ...

# Banco de preguntas precargado: LISTA DE DICCIONARIOS (no lo modifiques)
banco_preguntas = [
    {"pregunta": "Cual es la capital de Chile?", "respuesta": "Santiago"},
    {"pregunta": "Cuanto es 7 por 8?", "respuesta": "56"},
    {"pregunta": "Que palabra clave define una funcion en Python?", "respuesta": "def"},
    {"pregunta": "Cual es el simbolo del resto (modulo) en Python?", "respuesta": "%"},
    {"pregunta": "Que tipo de dato es 3.14?", "respuesta": "float"},
    {"pregunta": "Cuantos colores tiene el arcoiris?", "respuesta": "7"},
    {"pregunta": "Que funcion muestra texto en pantalla en Python?", "respuesta": "print"},
    {"pregunta": "Cual es el oceano que limita con Chile?", "respuesta": "Pacifico"},
]


def mostrar_pregunta(pregunta):
    print(pregunta["pregunta"])


def normalizar(texto):
    return texto.lower().strip()
    # INVESTIGA (2): metodos de string para normalizar.
    #   Busca: "python string lower", "python string strip".
    # TODO: retorna el texto ya normalizado.


def es_correcta(respuesta_usuario, respuesta_correcta):
    if normalizar (respuesta_usuario) == normalizar(respuesta_correcta):
        return True
    return False
    # Debe retornar True si las dos respuestas son iguales tras normalizar.
    # TODO: reusa normalizar() en ambos lados y compara con ==.


def jugar_ronda(jugador, banco, n): 
    puntaje = 0
    preguntas_elegidas = random.sample(banco_preguntas, n)
    for preguntas in preguntas_elegidas:
        mostrar_pregunta(preguntas)
    # Debe elegir n preguntas al azar del banco, jugarlas y retornar el puntaje.
    # INVESTIGA (1): usa random para elegir n preguntas al azar sin repetir.
    # TODO:
    #   1. elige n preguntas al azar del banco
    #   2. recorre las preguntas elegidas con un for
    #   3. por cada una: mostrar_pregunta(...), pide input, usa es_correcta(...)
    #   4. suma 1 al puntaje por cada acierto
    #   5. retorna el puntaje
    pass


def mostrar_ranking(jugadores):
    # Debe mostrar a los jugadores ordenados por puntaje de mayor a menor,
    # con su posicion, nombre, puntaje y porcentaje de aciertos.
    # INVESTIGA (3): ordenar con sorted usando key + reverse,
    #   y dar formato a un numero con dos decimales: f"{valor:.2f}".
    #   Busca: "python sorted key reverse", "python f-string 2 decimales".
    # TODO:
    #   1. ordena la lista de jugadores por su puntaje (mayor a menor)
    #   2. recorre los jugadores ordenados
    #   3. calcula el porcentaje = puntaje / preguntas * 100 (cuida dividir por 0)
    #   4. muestra posicion, nombre, puntaje y porcentaje con :.2f
    pass


def main():
    print("=== JUEGO DE TRIVIA POR RONDAS ===")
    preguntas_por_ronda = 5

    # Lectura protegida con try/except (ya resuelto, no lo cambies)
    try:
        cantidad_jugadores = int(input("Cuantos jugadores van a jugar? "))
    except ValueError:
        print("Entrada invalida. Se asume 1 jugador.")
        cantidad_jugadores = 1

    jugadores = []
    numero = 1
    while numero <= cantidad_jugadores:
        nombre = input(f"\nNombre del jugador {numero}: ")
        # TODO: llama a jugar_ronda(...) y guarda el puntaje en una variable
        # TODO: agrega a la lista jugadores un dict con las claves
        #       'nombre', 'puntaje' y 'preguntas'
        numero = numero + 1

    mostrar_ranking(jugadores)
    print("\nGracias por jugar!")


main()
