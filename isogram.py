word = input('Please put in a word: ')

def check(word):
    for letter in word:
        duplicates = word.count(letter)

    if duplicates != 1:
        print('This is not an isogram')
    else:
        print('This is an isogram')

check(word) 