
days = ['first', 'second', 'thrid', 'fourth', 'fifth', 'six',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
gifts = ['a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens',
        'four Calling Birds', 'five Golden Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming',
        'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping',
        'twelve Drummers Drumming']

def lyrics(startVerse, endVerse):
    global gifts
    gifts.reverse()
    return [f'On the {days[k-1]} day of Christmas my true love gave to me: {", ".join(gifts[12-k:11])}{(", and " if k > 1 else "")}{gifts[11]}.' for k in range(startVerse, endVerse+1)]


print(lyrics(1, 12))