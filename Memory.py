import random


card_values= []

for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
    
random.shuffle(card_values)
print(card_values)

card_values=[card_values[:6],card_values[6:12],card_values[12:18],card_values[18:24],card_values[24:30],card_values[30:36]]

ast= []


for i in range(1,37):
    ast += ["*"]

ast = [ast[:6],ast[6:12],ast[12:18],ast[18:24],ast[24:30],ast[30:36]]
for i in ast:
    print()
    for j in i:
        print(j,end=" ")
       
