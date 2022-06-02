times = []

while True:
    userInput = input()
    userInput = int( userInput )
    if ( userInput < 0 ):
        break
    times.append( userInput )

md = sum( times ) / len( times )
print( f"MEDIA: {md :.2f}" )

for time in times:
    if time < md:
        print(time)