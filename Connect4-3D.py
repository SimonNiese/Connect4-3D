import GameBoard as Game
from SimpleAI import AI

player1 = input("Enter Player 1: ")
player2 = input("Enter Player 2: ")

while player1 == player2:
    print("Players cannot have the same name!")
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")

print(player1, "vs.", player2)
print()

board = Game.GameBoard()
game_over = False
counter = 0

if player2 == "AI":
    while not game_over:
        if counter % 2 == 0:
            while True:
                try:
                    print()
                    print(player1)
                    coords = input("Place a piece [x,y]: ")
                    x = int(coords.split(",")[0].strip())
                    y = int(coords.split(",")[1].strip())
                    board.place(x, y, player1)
                    counter += 1
                    if board.check_for_win(player1):
                        print(player1, " wins!")
                        game_over = True
                except:
                    print("Try again")
                    continue
                break
        else:
            ai = AI()
            x, y = ai.make_decision(board.board)
            board.place(x, y, player2)
            counter += 1
            if board.check_for_win(player1):
                print(player2, " wins!")
                game_over = True
else:
    if counter % 2 == 0:
        while True:
            try:
                print()
                print(player1)
                coords = input("Place a piece [x,y]: ")
                x = int(coords.split(",")[0].strip())
                y = int(coords.split(",")[1].strip())
                board.place(x, y, player1)
                counter += 1
                if board.check_for_win(player1):
                    print(player1, " wins!")
                    game_over = True
            except:
                print("Try again")
                continue
            break
    else:
        while True:
            try:
                print()
                print(player2)
                coords = input("Place a piece [x,y]: ")
                x = int(coords.split(",")[0].strip())
                y = int(coords.split(",")[1].strip())
                board.place(x, y, player2)
                counter += 1
                if board.check_for_win(player2):
                    print(player2, " wins!")
                    game_over = True
            except:
                print("Try again")
                continue
            break