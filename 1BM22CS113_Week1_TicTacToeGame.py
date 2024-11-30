def checkpos(x, r, c):
    if 0 <= r <= 2 and 0 <= c <= 2:
        if x[r][c] != "X" and x[r][c] != "O":
            return True
    return False

def checkwinner(x):
    for i in range(3):
        j = 0
        if x[i][j] == x[i][j+1] == x[i][j+2] != '-':
            return True
        elif x[j][i] == x[j+1][i] == x[j+2][i] != '-':
            return True
        elif(x[0][0] == x[1][1] == x[2][2] != '-'  or x[0][2] == x[1][1] == x[2][0] != '-'):
            return True
    return False
        
def checkdraw(n):
    if n == 9:
        return True
    return False

def display(x):
    for i in range(3):
        print(x[i])

def initialise():
    x = []
    for i in range(3):
        l = []
        for j in range(3):
            l.append("-")
        x.append(l)
    return x

def main():
    count = 0
    gameover = False
    x = initialise()
    while count < 9:
        while count%2 == 0:
            print("Player X's turn: ")
            r = int(input("Enter row: "))
            c = int(input("Enter column: "))
            if checkpos(x, r, c):
                x[r][c] = 'X'
                count += 1
                display(x)
                if checkwinner(x):
                    print("Player X won!")
                    gameover = True
                    break
            else:
                continue
        if checkdraw(count):
            print("It's a draw")
            break
        if gameover:
            break

        while count%2 == 1:
            print("Player O's turn: ")
            r = int(input("Enter row: "))
            c = int(input("Enter column: "))
            if checkpos(x,r,c):
                x[r][c] = 'O'
                display(x)
                count += 1
                if checkwinner(x):
                    print("Player O won!")
                    gameover = True
                    break
            else:
                continue
        if checkdraw(count):
            print("It's a draw")
            break
        if gameover:
            break
main()
