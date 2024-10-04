import random


card_values= []

for i in range(1,19):
    card_values+= [i]
    card_values+= [i]
    
random.shuffle(card_values)
print(card_values)

cards_list = [card_values[:6],card_values[6:12],card_values[12:18],card_values[18:24],card_values[24:30],card_values[30:36]]
print(cards_list)

card_intervalsstart = 0
card_intervalsfinish = 6
cards_list2 = []

while card_intervalsfinish <= 36:
    new_item = card_values[card_intervalsstart:card_intervalsfinish]
    cards_list2 += [new_item]
    card_intervalsstart += 6
    card_intervalsfinish += 6

print(cards_list2)


#ast= []


'''for i in range(1,37):
    ast += ["*"]

ast = [ast[:6],ast[6:12],ast[12:18],ast[18:24],ast[24:30],ast[30:36]]
for i in ast:
    print()
    for j in i:
        print(j,end=" ")
       '''
