def convert():
    number = int(input('Please pick a number: '))
    pling = number % 3
    plang = number % 5
    plong = number % 7
    if pling == 0 and plang == 0 and plong == 0:
        print('PlingPlangPlong')
    elif pling == 0 and plang == 0:
        print('PlingPlang')
    elif pling == 0 and plong== 0:
        print('PlingPlong')
    elif pling == 0:
        print('Pling')
    elif plang == 0 and plong == 0:
        print('PlangPlong')
    elif plang == 0:
        print('Plang')
    elif plong == 0:
        print('Plong')
    else:
        print(number)

convert()