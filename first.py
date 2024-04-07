tab = input("name, age > ").split(',')

isAdult = True if int(tab[1]) >=18 else False

if isAdult:
    print(f'Hi {tab[0].capitalize()}, you\'re an adult !')

else:
    print(f'Hi {tab[0].capitalize()}, you\'re a child !')

