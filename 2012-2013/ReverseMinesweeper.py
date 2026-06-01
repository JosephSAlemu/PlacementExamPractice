
def addOne(input: str) -> str:
    if input == "X":
        return input
    elif input == "-":
        return "1"
    else:
        return str(int(input) + 1)

if __name__ == "__main__":
    arg = input()
    arg = arg.split(" ")
    x, y = int(arg[0]), int(arg[1])
    board = []
    for i in range(x):
        line = input()
        line = line.split(" ")
        board.append(line)


    res = []
    for row in range(x):
        rowL = []
        for col in range(y):
            rowL.append("-")
        res.append(rowL)

    for row in range(x):
        for col in range(y):
            if int(board[row][col]) == 1:
                res[row][col] = "X"

                if row - 1 >= 0:
                    res[row-1][col] = addOne(res[row-1][col])
                    
                    if col - 1 >= 0:
                        res[row-1][col-1] = addOne(res[row-1][col-1])

                    if col + 1 < y:
                        res[row-1][col+1] = addOne(res[row-1][col+1])

                if row + 1 < x:
                    res[row+1][col] = addOne(res[row+1][col])

                    if col - 1 >= 0:
                        res[row+1][col-1] = addOne(res[row+1][col-1])

                    if col + 1 < y:
                        res[row+1][col+1] = addOne(res[row+1][col+1])

                if col - 1 >= 0:
                    res[row][col-1] = addOne(res[row][col-1])

                if col + 1 < y:
                    res[row][col+1] = addOne(res[row][col+1])

    for row in res:
        print(*row, sep="")