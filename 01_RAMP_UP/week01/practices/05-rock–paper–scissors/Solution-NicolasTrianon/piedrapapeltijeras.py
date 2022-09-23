from random import choice
import random 

opciones = ["piedra", "papel", "tijeras"]
partidas_validas = [3, 5, 7, 9]

machine_choice = random.choice(opciones)

def your_choice():
    partidas = int(input("Elige el número de rondas: "))
    if partidas not in partidas_validas:
        print("Please choose a valid option")
        partidas = int(input("Elige el número de rondas: "))
    else:
        pass

    option_chosen = input("What will be your move? ")
    if option_chosen not in opciones:
        print("Please choose a valid option")
        option_chosen = input("What will be your move? ")
    else:
        pass

    partidas_ganador = ((partidas/2)+0.5)
    machine_games = 0
    human_games = 0
    
    while machine_games < partidas_ganador or human_games < partidas_ganador:
        option_chosen = input("What will be your move? ")
        while option_chosen not in opciones:
            print("Please choose a valid option")
            option_chosen = input("What will be your move? ")
        print("Your choice is " + option_chosen)
        print("Machine choice is " + machine_choice)
        if machine_choice ==  option_chosen:
            print("It´s a tie")
        elif (machine_choice == "piedra" and option_chosen == "tijeras") or (machine_choice == "tijeras" and option_chosen == "papel") or (machine_choice == "papel" and option_chosen == "piedra"): 
                print("Machine wins")
                machine_games += 1
                print("Machine = " + str(machine_games))
        else:
            print("Human wins")
            human_games += 1
            print("Human = " + str(human_games))
        if machine_games >= partidas_ganador:
            print("The winner is the Machine")
            break
        elif human_games >= partidas_ganador:
            print("The winner is the human")
            break

your_choice()