import random

card_values= []

for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
    
random.shuffle(card_values)
print(card_values)



def draw(n):
    for i in range(n):
        print(i)
        for j in range(n-1):
            print("* ", end="")

            
draw(7)
p1= 0
p2 = 0