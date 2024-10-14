import random

#Genera los valores de las cartas en la lista card_values y las mezcla usando random
card_values= []
for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
random.shuffle(card_values)
#print(card_values) #Prueba (borrar luego)

#Asigna los valores de asteriscos en la lista asterisc_values. 36 asteriscos en total 
asterisc_values = []
for i in range(1,37):
    asterisc_values += ["*"]

def turn(x,y): #Funcion para cambiar el asterisco por el valor
    asterisc_list[x][y] = cards_list[x][y]

#Esta funcion se encarga de generar las listas 2D usando los intervalos de 6 en 6 y un while loop. Como parametro toma una lista original, que en este caso puede ser card_values o asterisc_values.
def sublist_generator(original_list):
    intervalStart = 0 #Interval start y finish son para dividir las listas originales en los intervalos de 6 en 6 
    intervalFinish = 6
    new_list = [] #La nueva lista se generará aquí 
    while intervalFinish <= 36: #El while loop se va a llevar acabo hasta que intervalFinish sea 36, el total de fichas en el tablero
        new_item = original_list[intervalStart:intervalFinish] #Aquí creamos la variable new_item que va a tomar los intervalos de 6 en 6 de la lista original
        new_list += [new_item] #Metemos el new_item a la nueva lista
        intervalStart += 6 #Actualizamos los intervals
        intervalFinish += 6
    return new_list #Regresamos la nueva lista



cards_list = sublist_generator(card_values) #Para crear la lista 2D de cartas usamos la funcion generadora con el parametro de card_values
#print(cards_list) #Prueba

asterisc_list = sublist_generator(asterisc_values) #Hacemos lo mismo, para crear la lista 2D de asteriscos 

print("Welcome to Memory game!")
print("Created by: Adolfo Hernández and Alonso Arechiga")
print("-----------------------")
#mainMenu_option = mainMenu()
while True:
    print("Main menu")
    mainMenu_selection = int(input("Select an option: 1. Play / 2. Read rules / 3. Exit: "))
    
    if mainMenu_selection == 1:
        #Game
        print("Game")
    elif mainMenu_selection == 2:
        print("Memory game rules!")
        print("------------------")
        print("In memory game, a board is set with a bunch of cards flipped facing downward. Two players take turns flipping over two cards with the objective of matching them.")
        print("If the player flips the two cards and they match they get a point and the cards stay facing upwards. If they don't match, then they are flipped over again and the player gets no points")
        print("The game ends when all the cards are discovered, and the player with the most points win.")
        print("Do you want to play?")
        selection = int(input("1. Play / 2. Back to main menu: "))
        while selection != 1 and selection != 2:
            print("Invalid option, try again")
            selection = int(input("1. Play / 2. Back to main menu: "))
        if selection == 1:
            # Game 
            print("Game")
        else:
            continue

    elif mainMenu_selection == 3:
        exit()
        
