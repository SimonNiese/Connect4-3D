import numpy as np
import GamePiece

class GameBoard:
    def __init__(self):
        self.board = np.empty((4, 4, 4), dtype=GamePiece.GamePiece)
        for x in range(0, 4):
            for y in range(0, 4):
                for z in range(0, 4):
                    self.board[x, y, z] = GamePiece.GamePiece(active=False, player="none")


    def place(self, x, y, player):
        # Place a piece on the board. Pieces fall to the lowest available space on the z-axis
        if self.board[x, y, 0].active is False:
            self.board[x, y, 0] = GamePiece.GamePiece(True, player)
            print(player, " placed a piece on ", x, y, 0)
        elif self.board[x, y, 1].active is False:
            self.board[x, y, 1] = GamePiece.GamePiece(True, player)
            print(player, " placed a piece on ", x, y, 1)
        elif self.board[x, y, 2]. active is False:
            self.board[x, y, 2] = GamePiece.GamePiece(True, player)
            print(player, " placed a piece on ", x, y, 2)
        elif self.board[x, y, 3]. active is False:
            self.board[x, y, 3] = GamePiece.GamePiece(True, player)
            print(player, " placed a piece on ", x, y, 3)
        else:
            # If this is hit, there are no more available spaces for these coordinates
            print("Piece cannot be placed here")
            raise Exception()

    def check_for_win(self, player):
        # Check all parallel line all axis'
        for x in range(0, 4):
            for y in range(0, 4):
                if (self.board[x, y, 0].player is player
                and self.board[x, y, 1].player is player
                and self.board[x, y, 2].player is player
                and self.board[x, y, 3].player is player):
                    return True

            for z in range(0, 4):
                if (self.board[x, 0, z].player is player
                and self.board[x, 1, z].player is player
                and self.board[x, 2, z].player is player
                and self.board[x, 3, z].player is player):
                    return True

        for y in range(0, 4):
            for z in range(0, 4):
                if (self.board[0, y, z].player is player
                and self.board[1, y, z].player is player
                and self.board[2, y, z].player is player
                and self.board[3, y, z].player is player):
                    return True

        # Check all diagonal lines across y- and z-axis
        for x in range(0, 4):
            if (self.board[x, 0, 0].player is player
            and self.board[x, 1, 1].player is player
            and self.board[x, 2, 2].player is player
            and self.board[x, 3, 3].player is player):
                return True

            if (self.board[x, 0, 3].player is player
            and self.board[x, 1, 2].player is player
            and self.board[x, 2, 1].player is player
            and self.board[x, 3, 0].player is player):
                return True

        # Check all diagonal lines across x- and z-axis
        for y in range(0, 4):
            if (self.board[0, y, 0].player is player
            and self.board[1, y, 1].player is player
            and self.board[2, y, 2].player is player
            and self.board[3, y, 3].player is player):
                return True

            if (self.board[0, y, 3].player is player
            and self.board[1, y, 2].player is player
            and self.board[2, y, 1].player is player
            and self.board[3, y, 0].player is player):
                return True

        # Check all diagonal lines across x- and y-axis
        for z in range(0, 4):
            if (self.board[0, 0, z].player is player
            and self.board[1, 1, z].player is player
            and self.board[2, 2, z].player is player
            and self.board[3, 3, z].player is player):
                return True

            if (self.board[0, 3, z].player is player
            and self.board[1, 2, z].player is player
            and self.board[2, 1, z].player is player
            and self.board[3, 0, z].player is player):
                return True

        # Check diagonal lines across all axis'
        if (self.board[0, 0, 0].player is player
        and self.board[1, 1, 1].player is player
        and self.board[2, 2, 2].player is player
        and self.board[3, 3, 3].player is player):
            return True

        if (self.board[0, 3, 0].player is player
        and self.board[1, 2, 1].player is player
        and self.board[2, 1, 2].player is player
        and self.board[3, 0, 3].player is player):
            return True

        if (self.board[0, 0, 3].player is player
        and self.board[1, 1, 2].player is player
        and self.board[2, 2, 1].player is player
        and self.board[3, 3, 0].player is player):
            return True

        if (self.board[3, 0, 0].player is player
        and self.board[2, 1, 1].player is player
        and self.board[1, 2, 2].player is player
        and self.board[0, 3, 3].player is player):
            return True
        # Return false if no lines where completed
        return False
