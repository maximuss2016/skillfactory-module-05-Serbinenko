field = [["*", "1", "2", "3"],
         ["1", " ", " ", " "],
         ["2", " ", " ", " "],
         ["3", " ", " ", " "]]


def show():
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end="  ")
        print()


def ask(step):
    x, y = 0, 0
    print("ходит " + step)
    while True:
        x = int(input("Введите № строки: "))
        y = int(input("Введите № столбца: "))
        if  x > 3 or x < 1 or  y > 3 or y < 1 or field[x][y] == "X" or field[x][y] == "0":
            print("Вы ввели неверные координаты!")
        else:
            field[x][y] = step
            break
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end="  ")
        print()
    return


def chek_win(step):
    if field[1][1] == field[1][2] == field[1][3] == step \
            or field[2][1] == field[2][2] == field[2][3] == step \
            or field[3][1] == field[3][2] == field[3][3] == step \
            or field[1][1] == field[2][1] == field[3][1] == step \
            or field[1][2] == field[2][2] == field[3][2] == step \
            or field[1][3] == field[2][3] == field[3][3] == step \
            or field[1][1] == field[2][2] == field[3][3] == step \
            or field[1][3] == field[2][2] == field[3][1] == step:
        print(step + ' победил')
        return True

    if not (any([" " in row for row in field])):
        print("ничья")
        return True


show()

while True:
    ask('X')
    if chek_win('X'):
        break
    ask('O')
    if chek_win("O"):
        break