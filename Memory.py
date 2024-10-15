import random

#Genera los valores de las cartas en la lista card_values y las mezcla usando random
card_values= []
for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
random.shuffle(card_values)
print(card_values) #Prueba (borrar luego)

#Asigna los valores de asteriscos en la lista asterisc_values. 36 asteriscos en total 
asterisc_values = []
for i in range(1,37):
    asterisc_values += ["*"]

def turn(x,y): #Funcion para cambiar el asterisco por el valor
    asterisc_list[x][y] = cards_list[x][y]
    for i in asterisc_list: 
        print()
        for j in i:
            print(j,end=" ") #Se imprime el tablero

def board():
    for i in asterisc_list: 
        print()
        for j in i:
            print(j,end=" ") #Se imprime el tablero
    
def correct(y1,x1,y2,x2):
    if cards_list[y1][x1] == cards_list[y2][x2]:
        asterisc_list[y1][x1] = cards_list[y1][x1]
        asterisc_list[y2][x2] = cards_list[y2][x2]
    else:
        asterisc_list[y1][x1] = "*"
        asterisc_list[y2][x2] = "*"
        
def equal(y,x):
    if asterisc_list[y][x] != "*":
        count=+1
    else:
        count=+0
    return count


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
print(cards_list) #Prueba

asterisc_list = sublist_generator(asterisc_values) #Hacemos lo mismo, para crear la lista 2D de asteriscos 


p1= 0
p2= 0 #Variables jugadores
count= 0
decision= ""

board()

while True:
    print()
    print("--Player 1 turn--")
    print()
    y1= int(input("Type the number on the y axis: ")) -1
    x1= int(input("Type the number on the x axis: ")) -1 #Se preguntan las coordenadas
    if y1 > 6 or x1 > 6:
        print("Invalid syntax")
        continue
    equal(y1,x1)
    turn(y1,x1)
    print()
    y2= int(input("Type the number on the y axis: ")) -1
    x2= int(input("Type the number on the x axis: ")) -1 #Se preguntan las segundas coordenadas
    if y2 > 6 or x2 > 6:
        print("Invalid syntax")
        continue
    equal(y2,x2)
    turn(y2,x2)
    print()
    if cards_list[y1][x1] == cards_list[y2][x2]:
        if count > 0:
            p1 += 0
            print(count)
            print("You typed numbers that were already unveiled, cheater")
        else:
            p1 += 1
            print(f"You got 1 point!, you now have {p1} points")
    else:
        p1 += 0
        asterisc_list[y1][x1] = "*"
        asterisc_list[y2][x2] = "*"
        print(f"You got it wrong, you still hace {p1} points")
    print()
    print("--Player 2 turn--")
    print()
    y1= int(input("Type the number on the y axis: ")) -1
    x1= int(input("Type the number on the x axis: ")) -1 #Se preguntan las coordenadas
    if y1 > 6 or x1 > 6:
        print("Invalid syntax")
        continue
    equal(y1,x1)
    turn(y1,x1)
    print()
    y2= int(input("Type the number on the y axis: ")) -1
    x2= int(input("Type the number on the x axis: ")) -1 #Se preguntan las segundas coordenadas
    if y2 > 6 or x2 > 6:
        print("Invalid syntax")
        continue
    equal(y1,x2)
    turn(y2,x2)
    print()
    if cards_list[y1][x1] == cards_list[y2][x2]:
        if count > 0:
            p2 += 0
            count = 0
            print("You typed numbers that were already unveiled")
        else:
            p2 += 1
            print(f"You got 1 point!, you now have {p2} points")
    else:
        p2 += 0
        asterisc_list[y1][x1] = "*"
        asterisc_list[y2][x2] = "*"
        print(f"You got it wrong, you still hace {p2} points")
    print("Do you want to continue?")
    decision = input("Press C to continue or E to exit") 
    if p1+p2 == 18 or decision == "E":
        break
    else:
        continue


print("GAME OVER")
if p1 > p2:
    print(f"Player 1 points: {p1}")
    print(f"Player 2 pointa: {p2}")
    print("Congratulations Player 1, you won!!!")
elif p2 > p1:
    print(f"Player 1 points: {p1}")
    print(f"Player 2 pointa: {p2}")
    print("Congratulations Player 2, you won!!!")
else:
    print(f"Player 1 points: {p1}")
    print(f"Player 2 pointa: {p2}")
    print("You tied!")
    
