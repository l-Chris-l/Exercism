highScores = []
addingScores = ''

while addingScores.lower() != 'no':
    scores = input('Please enter a high score: ')
    highScores.append(scores)
    addingScores = input('Would you like to add another? ')

def highestScore():
    highest = max(highScores)
    print('The highest score is ' + highest)

def lastAdded():
    last = highScores[-1]
    print('The last high score is ' + last)

def top3():
    top3 = sorted(highScores, reverse=True)
    print(top3)
    print(top3[0], top3[1], top3[2])



highestScore()
lastAdded()
top3()