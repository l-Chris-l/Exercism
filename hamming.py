leftStrand = input('Please enter first DNA strand: ').upper()
rightStrand = input('Please enter second DNA strand: ').upper()

def check(leftStrand, rightStrand):
    differences = 0
    if len(leftStrand) != len(rightStrand):
        raise Exception('Strand lengths don\'t match')

    for x, y in zip(leftStrand, rightStrand):
            if x != y:
                differences += 1
            
    print('The Hamming Distance is ' + str(differences))

check(leftStrand, rightStrand)