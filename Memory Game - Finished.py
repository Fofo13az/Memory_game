import random

card_values= []
for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
random.shuffle(card_values)

asterisc_values = []
for i in range(1,37):
    asterisc_values += ["*"]

def turn(x,y): 
    asterisc_list[x][y] = cards_list[x][y]
    board()
    guess = cards_list[x][y]
    return guess

def unturn(x1, y1, x2, y2):
    asterisc_list[x1][y1] = "*"
    asterisc_list[x2][y2] = "*"
    board()

def board():
    row = 1
    print("  1 2 3 4 5 6")
    for i in asterisc_list: 
        if row != 1:
            print()
        print(row, end=" ")
        row += 1
        for j in i:
            print(j,end=" ") 

def sublist_generator(original_list):
    intervalStart = 0 
    intervalFinish = 6
    new_list = [] 
    while intervalFinish <= 36: 
        new_item = original_list[intervalStart:intervalFinish] 
        new_list += [new_item] 
        intervalStart += 6 
        intervalFinish += 6
    return new_list 

def game(playername):
    player_score = 0
    global numbers_foundList
    while True:
        print()
        print(f"--{playername} turn--")
        print()
        y1= int(input("Select the first row!: ")) -1
        x1= int(input("Select the first column!: ")) -1 
        print()
        if y1 >= 6 or x1 >= 6 or y1+1<=0 or x1+1<= 0:
            print("Invalid syntax")
            continue
        guess1_value = turn(y1,x1)
        print()
        y2= int(input("Select the second row!: ")) -1
        x2= int(input("Select the second column!: ")) -1 
        if y2 >= 6 or x2 >= 6 or y2+1<=0 or x2+1<= 0:
            print("Invalid syntax")
            continue
        print()
        guess2_value = turn(y2,x2)
        print()
        if guess1_value != guess2_value:
            print()
            print("Incorrect!")
            print()
            unturn(y1, x1, y2, x2)
            player_score += 0
            break
        else:
            if guess1_value not in numbers_foundList and guess2_value not in numbers_foundList:
                player_score += 1
                numbers_foundList.append(guess1_value)
                numbers_foundList .append(guess2_value)
                break
            else:
                player_score += 0
                print("Cheater! You get no points.")
                break
    return player_score


cards_list = sublist_generator(card_values) 
asterisc_list = sublist_generator(asterisc_values) 
player1 = 0
player1Name = "Player 1"
player2 = 0 
player2Name = "Player 2"
numbers_foundList = []

print("Welcome to Memory game!")
print("Created by: Adolfo Hernández and Alonso Arechiga")
print("-----------------------")

while True:

    print("Main menu")
    mainMenu_selection = int(input("Select an option: 1. Play / 2. Read rules / 3. Exit: "))
    
    if mainMenu_selection == 1:
        #print(cards_list)
        board()
        while True:
            player1 += game(player1Name)
            player2 += game(player2Name)
            print()
            print(f"Current score: Player 1: {player1} | Player 2: {player2}")
            decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
            while decision != 1 and decision != 2:
                print("Please select a valid option")
                decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
            else:
                if decision == 1:
                    continue
                else:
                    print("Thanks for playing Memory Game!")
                    exit()      
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
            #print(cards_list)
            board()
            while True:
                player1 += game(player1Name)
                player2 += game(player2Name)
                print()
                print(f"Current score: Player 1: {player1} | Player 2: {player2}")
                decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
                while decision != 1 and decision != 2:
                    print("Please select a valid option")
                    decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
                else:
                    if decision == 1:
                        continue
                    else:
                        print("Thanks for playing Memory Game!")
                        exit()
        else:
            continue
    elif mainMenu_selection == 3:
        print("Thank you for playing Memory Game!")
        exit()
    else:
        print("Invalid option. Please select a valid option.")
        continue