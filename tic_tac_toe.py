print("#"*7,"Игра крестики - нолики", "#"*7)
game_map = [[i,"-", "-", "-"] for i in range(3)]

def game_board(board, rows = 3, cols = 4):
    for i in range(rows):
        for j in range(cols):
            print(board[i][j], end=" ")
        print()

def check_win(board):
    for row in board:
        if row[1] == row[2] == row[3] and row[1] != "-":
            return row[1]
    for col in range(1, 4):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return board[0][col]

    # проверка диагоналей
    if board[0][1] == board[1][2] == board[2][3] and board[0][1] != "-":
        return board[0][1]
    if board[0][3] == board[1][2] == board[2][1] and board[0][3] != "-":
        return board[0][3]

    return None

def begin(start_symbol):
    global game_map
    while True:
        if start_symbol == "x":
            a = int(input("введите число от 0 до 2"))
            b = int(input("введите число от 1 до 3"))
            if (a < 0 or a > 2) or (b < 1 or b > 3):
                print("Попробуйте еще раз")
            else:
                if game_map[a][b] == "-":
                    game_map[a][b] = start_symbol
                    print()
                    print(" ", 1, 2, 3)
                    game_board(game_map)
                    print("Ход другого игрока")
                    start_symbol = "0"
                else:
                    print("Попробуйте другую позицию")
        elif start_symbol == "0":
            a = int(input("введите число от 0 до 2"))
            b = int(input("введите число от 1 до 3"))
            if (a < 0 or a > 2) or (b < 1 or b > 3):
                print("Попробуйте еще раз")
            else:
                if game_map[a][b] == "-":
                    game_map[a][b] = start_symbol
                    print()
                    print(" ", 1, 2, 3)
                    game_board(game_map)
                    print("Ход другого игрока")
                    start_symbol = "x"
                else:
                    print("Попробуйте другую позицию")
        check_win(game_map)
        if check_win(game_map) == "x":
            print("Выйграл X")
            break
        if check_win(game_map) == "0":
            print("Выйграл 0")
            break

print()
print(" ", 1, 2, 3)
game_board(game_map)
print()
start = input("Введите символ с которого хотите начать(x/0): ")

if start == "x":
    begin("x")
elif start == "0":
    begin("0")
else:
    print("Введите корректный символ: ")




