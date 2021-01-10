direction = ""

while direction != 'q':
    direction = (input("Do you want to go (N)orth, (S)outh, (E)ast or (W)est? ")).lower()
    if direction == "n":
        print("You head north, into the forest")
    elif direction == 's':
        print("The coast blocks your path south.")
    elif direction == 'w':
        print('The western fileds are comforting to walk through.')
    elif direction == 'e':
        print('You were eaten by a grue')
    elif direction == 'q':
        print("Quitting the game")
    else:
        print("I didn't recognise your choice")
        
import datetime
dt =  datetime.datetime.now()

print(dt.hour)