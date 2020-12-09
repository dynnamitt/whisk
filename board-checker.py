
my_board1 = ["x", "o", "x",
            "x", "x", "o",
            None, "o", "x"]

my_board2 = ["e", "o", "x",
            "e", None, "o",
            "e",  "o", None]


def horiz_result(board: list, start: int) -> str:
    if board[start] == board[start+1] == board[start+2]:
        return board[start]


def vert_result(board: list, start: int) -> str:
    if board[start] == board[start+3] == board[start+6]:
        return board[start]


def diagonal_result(board: list, dir="L") -> str:
    if dir == "L":
        start = 0
        jumps = [4, 8]
    else:
        start = 2
        jumps = [2, 2]

    if board[start] == board[start+jumps[0]] == board[start+jumps[1]]:
        return board[start]


def check_all(board: list) -> str:
    for x in [0, 3, 6]:
        win = horiz_result(board, x)
        if win:
            print("win at x =", x)
            return win

    for y in [0, 1, 2]:
        win = vert_result(board, y)
        if win:
            print("win at y =", y)
            return win

    for dir_ in ["Left", "Right"]:
        win = diagonal_result(board, dir_[0])
        if win:
            print("win at diagonal starting from ", dir_)
            return win

print("-------------------------------------------------")
print("1st Winner is: ", check_all(my_board1))
print("-------------------------------------------------")
print("2nd Winner is: ", check_all(my_board2))