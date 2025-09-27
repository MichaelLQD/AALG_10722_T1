import random

def crearEntrenadorPokemon(tipo):
    if tipo == 1:
        nombrej1 = input("Ingrese su nombre: ")
        nombrep1 = input("Ingrese el nombre de su Pokemon: ")
        ataque = random.randint(20, 100)
        vidamax = random.randint(150, 400)
        vidaac = vidamax
        jugador = [nombrej1, nombrep1, ataque, vidamax, vidaac]
    elif tipo == 2:
        nombrej2 = input("Ingrese el nombre del entrenador rival: ")
        nombrep2 = input("Ingrese el nombre del Pokemon rival: ")
        ataque = random.randint(20, 100)
        vidamax = random.randint(150, 400)
        vidaac = vidamax
        jugador = [nombrej2, nombrep2, ataque, vidamax, vidaac]
        print("\n--- Datos del Pokemon Rival ---")
        print(f"Entrenador: {nombrej2}")
        print(f"Pokemon: {nombrep2}")
        print(f"Ataque maximo: {ataque}")
        print(f"Vida maxima: {vidamax}")
    return jugador

def valorDeAtaque(tipo, pokemon):
    return random.randint(0, pokemon[2])

def defender(tipo, pokemon, ataque):
    prob = random.randint(1, 6)
    if prob == 6:
        daño = 0
    else:
        daño = ataque
    pokemon[4] -= daño
    return pokemon[4]

def recuperar(pokemon):
    pokemon[4] = pokemon[3]

def mostrarEstado(pokemon):
    print(f"{pokemon[0]} con {pokemon[1]} - Vida actual: {max(0, pokemon[4])}")

jugador = crearEntrenadorPokemon(1)
ganadas = 0
perdidas = 0

while True:
    print("\nMenu de pelea")
    opcion = input("Pelear(P) o Finalizar(F) ").strip().upper()

    if opcion == "F":
        print("\nFin de jueogo")
        print(f"Entrenador: {jugador[0]}")
        print(f"Pokemon: {jugador[1]}")
        print(f"Ataque maximo: {jugador[2]}")
        print(f"Vida maxima: {jugador[3]}")
        print(f"Encuentros ganados: {ganadas}")
        print(f"Encuentros perdidos: {perdidas}")
        break

    elif opcion == "P":
        rival = crearEntrenadorPokemon(2)
        recuperar(jugador)
        recuperar(rival)
        turno = 1

        while jugador[4] > 0 and rival[4] > 0:
            print("\nNuevo Turno ")
            if turno == 1:
                print(f"\n{jugador[0]} ataca con {jugador[1]}")
                ataque = valorDeAtaque(1, jugador)
                print(f"Ataque realizado: {ataque}")
                defender(2, rival, ataque)
                mostrarEstado(rival)
                turno = 2
            else:
                print(f"\n{rival[0]} ataca con {rival[1]}")
                ataque = valorDeAtaque(2, rival)
                print(f"Ataque realizado: {ataque}")
                defender(1, jugador, ataque)
                mostrarEstado(jugador)
                turno = 1

        print("\nResultado de la pelea")
        if jugador[4] > 0:
            print(f"¡{jugador[0]} gana con {jugador[1]}!")
            ganadas += 1
        else:
            print(f"¡{rival[0]} gana con {rival[1]}!")
            perdidas += 1

    else:
        print("Opcion ingresada no es valido, ingrese otro valorz ")
