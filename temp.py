def drawField():
    for row in range(5):
        if row%2 == 0:
            for column in range(5):
                    if column%2 == 0:
                        if column != 4:
                            print(" ", end = "")
                        else:
                            print(" ")
                    else:
                            print("|", end = "")
        else:
            print("-----")

Player = 1
currentField = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
print(currentField)
while(True):
    print("Players turn:", Player)
    MoveRow = int(input("Please, enter the row: "))
    MoveColumn = int(input("Please enter the column: "))
    if Player == 1:
        currentField[MoveColumn][MoveRow] = "X"
        Player = 2
    else:
        currentField[MoveColumn][MoveRow] = "O"
        Player = 1
    print(currentField)
