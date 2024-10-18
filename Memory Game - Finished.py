import random

#This function establishes the card values on the card_values list to then shuffle them with random
card_values= []
for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
random.shuffle(card_values)

#This function generates 36 asterisc on the asterisc_values list
asterisc_values = []
for i in range(1,37):
    asterisc_values += ["*"]

#This function turn changes an asterisc on asterisc_list to the card value it represents on the cards_values list
def turn(x,y): 
    asterisc_list[x][y] = cards_list[x][y]
    board()
    guess = cards_list[x][y]
    return guess

#This function turns back the asterisc values to asteriscs
def unturn(x1,y1,x2,y2):
    asterisc_list[x1][y1] = "*"
    asterisc_list[x2][y2] = "*"
    board()

#This function prints the board everytime, which is the modified asterisc_list
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

#This function generates a 2D list in an existing list on a interval of 6 in 6
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

#This function is the turn for each player
def game(playername):
    player_score = 0
    global numbers_foundList
    while True:
        print()
        print(f"--{playername} turn--")
        print()
        y1= int(input("Select the first row!: ")) -1
        x1= int(input("Select the first column!: ")) -1 #You select the first position you want
        print()
        if y1 >= 6 or x1 >= 6 or y1+1<=0 or x1+1<= 0: #Here it checks if the position is valid or not
            print("Invalid syntax")
            continue #If not, it ask you the position again
        guess1_value = turn(y1,x1) #This almacenates the first position
        print()
        if guess1_value in numbers_foundList: #It checks if the value is already opened
            print()
            print("Cheater! That one is already opened.")
            player_score = 0
            break
        y2= int(input("Select the second row!: ")) -1
        x2= int(input("Select the second column!: ")) -1  #You select the second position
        if y2 >= 6 or x2 >= 6 or y2+1<=0 or x2+1<= 0: #Here it checks if the position is valid or not
            print("Invalid syntax")
            continue #If not, it ask you the position again
        print()
        guess2_value = turn(y2,x2) #This almacenates the second position
        print()
        if guess2_value in numbers_foundList: #It checks if the value is already opened
            print()
            print("Cheater! That one is already opened.")
            player_score = 0
            asterisc_list[y1][x1] = "*" #It turns the original position back to asterisc
            board()
            break
        if x1 == x2 and y1 == y2: #Here it checks if you put the same position
            print("Cheater! You get no points.")
            unturn(y1,x1,y2,x2) #It turns back the values to asterisc
            player_score += 0 #You get 0 points
            break
        else: #If the position is different
            if guess1_value != guess2_value: #If the card values are not the same
                print()
                print("Incorrect!")
                print()
                unturn(y1,x1,y2,x2) #It turns back the values to asterisc
                player_score += 0 #You get 0 points
                break
            else: #If the card values are the same
                if guess1_value not in numbers_foundList and guess2_value not in numbers_foundList: #And the values are not in the found list
                    player_score += 1 #You get 1 point
                    numbers_foundList.append(guess1_value)
                    numbers_foundList.append(guess2_value) #The values get added to the found list
                    break
                else: #If the values are in the found list
                    player_score += 0
                    print("Cheater! You get no points.") #The player put repeated numbers so he gets no points
                    break
    return player_score #It returns if the player won any points


cards_list = sublist_generator(card_values) #It divides the card_list into 6 lists of 6 values each
asterisc_list = sublist_generator(asterisc_values) #It divides the asterisc_list into 6 lists of 6 values each
player1 = 0
player1Name = "Player 1"
player2 = 0
player2Name = "Player 2"
numbers_foundList = [] #A list that almacenats the values that were already found
mainMenu_selection = 0


print("Welcome to Memory game!")
print("Created by: Adolfo Hernández and Alonso Arechiga")
print("-----------------------")

while True:
    if mainMenu_selection == 3: #This is to end the loop if all cards have been turned up
        break
    print("Main menu")
    mainMenu_selection = int(input("Select an option: 1. Play / 2. Read rules / 3. Exit: "))
    if mainMenu_selection == 1: #If the player wants to play
        #print(cards_list) PRUEBA
        board()
        while True:
            player1 += game(player1Name)
            if player1 + player2 == 18: #If all cards have been turned up
                mainMenu_selection = 3 #It makes the menu selection 3 to break the first loop
                break #It ends this one
            player2 += game(player2Name) #It does a turn for each player
            if player1 + player2 == 18:
                mainMenu_selection = 3
                break
            print()
            print(f"Current score: Player 1: {player1} | Player 2: {player2}")
            decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
            while decision != 1 and decision != 2:
                print("Please select a valid option")
                decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
            else:
                if decision == 1: #It continues the game
                    continue
                else: #It stops the game
                    print("Thanks for playing Memory Game!")
                    break    
    elif mainMenu_selection == 2: #It prints the rules
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
        if selection == 1: #If the player wants to play
            #print(cards_list) PRUEBA
            board()
            while True:
                player1 += game(player1Name)
                if player1 + player2 == 18: #If all cards have been turned up
                    mainMenu_selection = 3 #It makes the menu selection 3 to break the first loop
                    break #It ends this one
                player2 += game(player2Name) #It does a turn for each player
                if player1 + player2 == 18:
                    mainMenu_selection = 3 
                    break
                print()
                print(f"Current score: Player 1: {player1} | Player 2: {player2}")
                decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
                while decision != 1 and decision != 2:
                    print("Please select a valid option")
                    decision = int(input("Do you want to continue? 1. Yes | 2. No: "))
                else:
                    if decision == 1: #It continues the game
                        continue
                    else: #It stops the game
                        print("Thanks for playing Memory Game!")
                        break
        else:
            continue
    elif mainMenu_selection == 3: #It stops the game
        print("Thank you for playing Memory Game!")
        break
    else:
        print("Invalid option. Please select a valid option.")
        continue

if player1 > player2: #Player 1 wins
    print(f"Player 1 points: {player1}")
    print(f"Player 2 pointa: {player2}")
    print("Congratulations Player 1, you won!!!")
elif player2 > player1: #player 2 wins
    print(f"Player 1 points: {player1}")
    print(f"Player 2 pointa: {player2}")
    print("Congratulations Player 2, you won!!!")
else: #Its a tie
    print(f"Player 1 points: {player1}")
    print(f"Player 2 pointa: {player2}")
    print("You tied!")
