from os import system

def main():
    turn = "X"

    board = [
        [11,12,13],
        [21,22,23],
        [31,32,33]
    ]

    win_positions = [
        ["11", "12", "13"],
        ["21", "22", "23"],
        ["31", "32", "33"],

        ["11", "21", "31"],
        ["12", "22", "32"],
        ["13", "23", "33"],

        ["11", "22", "33"],
        ["31", "22", "13"]
    ]    

    while True:
        system("clear")
        for row in board:
            print(row)

        print(f"\nVez de: {turn}")
        choice = input("Insira a jogada: ")    
        
        r = int(choice[0]) - 1
        c = int(choice[1]) - 1
        pos = board[r][c]

        if (pos == "X" or pos == "O"):
            continue
        else:
            board[r][c] = turn

        for combination in win_positions:
            c = combination

            pos1 = c[0]
            pos2 = c[1]
            pos3 = c[2]

            b = board

            b1 = b[int(pos1[0])-1][int(pos1[1])-1]
            b2 = b[int(pos2[0])-1][int(pos2[1])-1]
            b3 = b[int(pos3[0])-1][int(pos3[1])-1]

            if b1 == b2 == b3:
                print(turn, "ganhou!")
                return

        if (turn == "X"):
            turn = "O"
        else:
            turn = "X"

main()
