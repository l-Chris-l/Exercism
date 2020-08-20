def twoFer():
    name = input("Please enter a name: ")
    if name == '':
        print('One for you, one for me')
    else:
        print('One for ' + name + ', one for me.')

twoFer()