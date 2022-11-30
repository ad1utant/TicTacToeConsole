from time import sleep

#Initijalization
fields = [0,1,2,3,4,5,6,7,8,9]
won_positions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
x_list,o_list,used = [],[],[]
Range,won = 9,False

#Game board
def Board():
    for i in range(100):
        print()
    print("|-----------------|")
    print("|     |     |     |")
    print("|  ",fields[1],"  |  ",fields[2],"  |  ",fields[3],"  |",sep="")
    print("|     |     |     |")
    print("|-----------------|")
    print("|     |     |     |")
    print("|  ",fields[4],"  |  ",fields[5],"  |  ",fields[6],"  |",sep="")
    print("|     |     |     |")
    print("|-----------------|")
    print("|     |     |     |")
    print("|  ",fields[7],"  |  ",fields[8],"  |  ",fields[9],"  |",sep="")
    print("|     |     |     |")
    print("|-----------------|")

#Game loop
Board()
while Range > 0:
    if won:
        break

    x = int(input())

    #checking if fieled is busy
    if x in used:
        print('To pole jest już zajęte')
        Range += 1
        continue

    used.append(x)

    divisibility = len(used)
    if divisibility % 2 == 0:
        divisibility = 'X'
        x_list.append(x)
        x_list.sort()
    else:
        divisibility = 'O'
        o_list.append(x)
        o_list.sort()
    fields[x] = divisibility

    Board()

    #Checking if player won
    for element in won_positions:

        #O won algorithm
        if all(elem in o_list for elem in element):
            print('Wygrało kółko')
            won = True
            break

        #X won alghoritm
        if all(elem in x_list for elem in element):
            print('Wygrał krzyżyk')
            won = True
            break
    Range -= 1
#Draw
if won is False:
    Board()
    print('Remis')
#Close
print('program zamknie sie za 5 sekund')
sleep(5)