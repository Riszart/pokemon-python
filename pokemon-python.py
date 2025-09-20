import random
import os

class Pokemon:
    def __init__(self,nombre,tipo,energia):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia

    def ataca(self,rival):
        rival.energia -= random.randint(10,50)
        return f"{self.nombre} <=> Da un golpe \n{'_'*80}\n "
    
    def descansar(self):
        self.energia += 10
        return f"{self.nombre} <=> Guardó reposo \n Nivel de energía \n{'_'*80}\n"
    
    def mostrar_estado(self):
        return f"""
Estado del Pokémon
Nombre  :   {self.nombre}
Vida    :   {self.energia}
Tipo    :   {self.tipo}"""


def clear(): return 
    # if os.name == "nt":
    #     os.system("cls")

pokedes = [
    Pokemon("Pikachu","eléctrico",130),
    Pokemon("Bulbasaur","hierba",100),
    Pokemon("Charmander","fuego",105),
    Pokemon("Squirtle","agua",115)
]

def accion(atacante,rival):
    print(f"{'.'*46}\n [1] Atacar | [2] Descansar | [3] Estado\n{'.'*46}")
    while True:
        obs = input()
        if obs == "1": print(atacante.ataca(rival));return 
        elif obs == "2": print(atacante.descansar());break
        elif obs == "3": print(atacante.mostrar_estado())
        else: print("Opción no válida")
    
def batalla(pokemon1,entrenador1,pokemon2,entrenador2):
    iswin = ""
    while True:
        print(f"{'_'*80}\n{entrenador1:^60} : {pokemon1.nombre:>10} [{pokemon1.energia}]")
        accion(pokemon1,pokemon2)
        if pokemon2.energia <= 0:
            iswin = entrenador2
            break

        print(f"{'_'*80}\n{entrenador2:^60} : {pokemon2.nombre:>10} [{pokemon2.energia}]")
        accion(pokemon2,pokemon1)
        if pokemon1.energia <= 0:
            iswin = entrenador1
            break

    if iswin != "":
        print(f"\n{'*'*10} ¡El ganador es el {iswin}! {'*'*10}\n")

clear()
print(f"""
{'Elige un Pokémon':^46}\n{"-" * 46}
|{" ":^5}|{"Pokémon":^12}|{"Tipo":^12}|{"Energía":^12}|\n{"-" * 46}
|{"[0]":^5}|{pokedes[0].nombre:<12}|{pokedes[0].tipo.capitalize():^12}|{pokedes[0].energia:^12}|\n{"-" * 46}
|{"[1]":^5}|{pokedes[1].nombre:<12}|{pokedes[1].tipo.capitalize():^12}|{pokedes[1].energia:^12}|\n{"-" * 46}
|{"[2]":^5}|{pokedes[2].nombre:<12}|{pokedes[2].tipo.capitalize():^12}|{pokedes[2].energia:^12}|\n{"-" * 46}
|{"[3]":^5}|{pokedes[3].nombre:<12}|{pokedes[3].tipo.capitalize():^12}|{pokedes[3].energia:^12}|\n{"-" * 46}
""")
user1 = int(input("ENTRENADOR 1 : "))
print(f"ENTRENADOR 1 - eligió a => {pokedes[user1].nombre}\n{'*'*46}")
user2 = int(input("ENTRENADOR 2 : "))
print(f"ENTRENADOR 2 - eligió a => {pokedes[user2].nombre}\n{'*'*46}")
clear()
print(f"{'-'*80}\n{'Comienza la batalla'.upper():^80}")
batalla(pokedes[user1],"ENTRENADOR 1",pokedes[user2],"ENTRENADOR 2")
