import numpy as np

class AI:
    def __init__(self):
        pass

    def calculate_line(self, player, ai):
        if player == 0:
            match ai:
                case 0:
                    return 1
                case 1:
                    return 3
                case 2:
                    return 5
                case 3:
                    return 10
        elif ai == 0:
            match player:
                case 0:
                    return 1
                case 1:
                    return 2
                case 2:
                    return 3
                case 3:
                    return 5
        else:
            return 0

    def calculate_score(self, board, x, y, z):
        score = 0
        player = 0
        ai = 0

        # Calculate along x-axis
        for temp_x in range(4):
            if board[temp_x, y ,z].active is True:
                if board[temp_x, y, z].player == "AI":
                    ai += 1
                else:
                    player += 1
        score += self.calculate_line(player, ai)

        player = 0
        ai = 0

        # Calculate along y-axis
        for temp_y in range(4):
            if board[x, temp_y, z].active is True:
                if board[x, temp_y, z].player == "AI":
                    ai += 1
                else:
                    player += 1
        score += self.calculate_line(player, ai)

        player = 0
        ai = 0

        # Calculate along z-axis
        for temp_z in range(4):
            if board[x, y, temp_z].active is True:
                if board[x, y, temp_z].player == "AI":
                    ai += 1
                else:
                    player += 1
        score += self.calculate_line(player, ai)

        player = 0
        ai = 0

        # Calculate diagonally across x- and y-axis
        if x == y:
            for temp_xy in range(4):
                if board[temp_xy, temp_xy, z].active is True:
                    if board[temp_xy, temp_xy, z].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        # Calculate diagonally across x- and z-axis
        if x == z:
            for temp_xz in range(4):
                if board[temp_xz, y, temp_xz].active is True:
                    if board[temp_xz, y, temp_xz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        # Calculate diagonally across y- and z-axis
        if y == z:
            for temp_yz in range(4):
                if board[x, temp_yz, temp_yz].active is True:
                    if board[x, temp_yz, temp_yz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if x + y == 3:
            for temp_xy in range(4):
                if board[temp_xy, 3 - temp_xy, z].active is True:
                    if board[temp_xy, 3 - temp_xy, z].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if x + z == 3:
            for temp_xz in range(4):
                if board[temp_xz, y, 3 - temp_xz].active is True:
                    if board[temp_xz, y, 3 - temp_xz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if y + z == 3:
            for temp_yz in range(4):
                if board[x, temp_yz, 3 - temp_yz].active is True:
                    if board[x, temp_yz, 3 - temp_yz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if x == y and y == z:
            for temp_xyz in range(4):
                if board[temp_xyz, temp_xyz, temp_xyz].active is True:
                    if board[temp_xyz, temp_xyz, temp_xyz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if x == y and y + z == 3:
            for temp_xyz in range(4):
                if board[temp_xyz, temp_xyz, 3 - temp_xyz].active is True:
                    if board[temp_xyz, temp_xyz, 3 - temp_xyz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if x == z and y + z == 3:
            for temp_xyz in range(4):
                if board[temp_xyz, 3 - temp_xyz, temp_xyz].active is True:
                    if board[temp_xyz, 3 - temp_xyz, temp_xyz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)

            player = 0
            ai = 0

        if y == z and z + x == 3:
            for temp_xyz in range(4):
                if board[3 - temp_xyz, temp_xyz, temp_xyz].active is True:
                    if board[3 - temp_xyz, temp_xyz, temp_xyz].player == "AI":
                        ai += 1
                    else:
                        player += 1
            score += self.calculate_line(player, ai)
        return score

    def make_decision(self, board):
        decision_matrix = np.zeros((4, 4))
        for x in range(4):
            for y in range(4):
                if board[x, y, 3].active is True:
                    decision_matrix[x, y] = 0
                elif board[x, y, 2].active is True:
                    decision_matrix[x, y] = self.calculate_score(board, x, y, 3)
                elif board[x, y, 1].active is True:
                    decision_matrix[x, y] = self.calculate_score(board, x, y, 2)
                elif board[x, y, 0].active is True:
                    decision_matrix[x, y] = self.calculate_score(board, x, y, 1)
                else:
                    decision_matrix[x, y] = self.calculate_score(board, x, y, 0)

        highscore = 0
        high_x = 0
        high_y = 0

        for x in range(4):
            for y in range(4):
                if decision_matrix[x, y] > highscore:
                    highscore = decision_matrix[x, y]
                    high_x = x
                    high_y = y

        return high_x, high_y

