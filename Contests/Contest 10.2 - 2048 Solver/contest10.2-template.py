#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *


def AI(mat):
    import copy

    def compress(row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    def merge(row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(board):
        new_board = []
        for row in board:
            compressed = compress(row)
            merged = merge(compressed)
            final = compress(merged)
            new_board.append(final)
        return new_board

    def move_right(board):
        reversed_board = [row[::-1] for row in board]
        moved = move_left(reversed_board)
        return [row[::-1] for row in moved]

    def transpose(board):
        return [list(row) for row in zip(*board)]

    def move_up(board):
        transposed = transpose(board)
        moved = move_left(transposed)
        return transpose(moved)

    def move_down(board):
        transposed = transpose(board)
        moved = move_right(transposed)
        return transpose(moved)

    def is_valid_move(original, moved):
        return original != moved

    def score_board(board):
        max_tile = max(max(row) for row in board)
        corners = [board[0][0], board[0][-1], board[-1][0], board[-1][-1]]
        corner_bonus = max_tile if max_tile in corners else 0
        return corner_bonus

    directions = {
        'w': move_up,
        'a': move_left,
        's': move_down,
        'd': move_right
    }

    best_score = -1
    best_move = None

    for dir_key in ['w', 'a', 's', 'd']:
        moved = directions[dir_key](copy.deepcopy(mat))
        if is_valid_move(mat, moved):
            score = score_board(moved)
            if score > best_score:
                best_score = score
                best_move = dir_key

    return best_move

def AI(mat):
    import copy
    import math

    def compress(row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    def merge(row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(board):
        new_board = []
        for row in board:
            compressed = compress(row)
            merged = merge(compressed)
            final = compress(merged)
            new_board.append(final)
        return new_board

    def move_right(board):
        reversed_board = [row[::-1] for row in board]
        moved = move_left(reversed_board)
        return [row[::-1] for row in moved]

    def transpose(board):
        return [list(row) for row in zip(*board)]

    def move_up(board):
        transposed = transpose(board)
        moved = move_left(transposed)
        return transpose(moved)

    def move_down(board):
        transposed = transpose(board)
        moved = move_right(transposed)
        return transpose(moved)

    def is_valid_move(original, moved):
        return original != moved

    def count_empty(board):
        return sum(cell == 0 for row in board for cell in row)

    def max_in_corner(board):
        max_tile = max(max(row) for row in board)
        corners = [board[0][0], board[0][-1], board[-1][0], board[-1][-1]]
        return max_tile in corners

    def smoothness(board):
        penalty = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    continue
                for dx, dy in ((0, 1), (1, 0)):  # right and down
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj] != 0:
                        penalty += abs(math.log2(board[i][j]) - math.log2(board[ni][nj]))
        return -penalty  # negative penalty

    def monotonicity(board):
        def score_line(line):
            inc = dec = 0
            for i in range(3):
                if line[i] > line[i + 1]:
                    dec += line[i] - line[i + 1]
                else:
                    inc += line[i + 1] - line[i]
            return -min(inc, dec)
        
        total = 0
        for row in board:
            total += score_line(row)
        for col in zip(*board):
            total += score_line(col)
        return total

    def score_board(board):
        score = 0
        if max_in_corner(board):
            score += 10000  # reward high tile in corner
        score += count_empty(board) * 100
        score += smoothness(board) * 1.5
        score += monotonicity(board) * 1.0
        return score

    directions = {
        'w': move_up,
        'a': move_left,
        's': move_down,
        'd': move_right
    }

    best_score = float('-inf')
    best_move = None

    for dir_key in ['w', 'a', 's', 'd']:
        moved = directions[dir_key](copy.deepcopy(mat))
        if is_valid_move(mat, moved):
            score = score_board(moved)
            if score > best_score:
                best_score = score
                best_move = dir_key

    return best_move

def AI(mat):
    import copy
    import math

    def compress(row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    def merge(row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(board):
        new_board = []
        for row in board:
            compressed = compress(row)
            merged = merge(compressed)
            final = compress(merged)
            new_board.append(final)
        return new_board

    def move_right(board):
        reversed_board = [row[::-1] for row in board]
        moved = move_left(reversed_board)
        return [row[::-1] for row in moved]

    def transpose(board):
        return [list(row) for row in zip(*board)]

    def move_up(board):
        transposed = transpose(board)
        moved = move_left(transposed)
        return transpose(moved)

    def move_down(board):
        transposed = transpose(board)
        moved = move_right(transposed)
        return transpose(moved)

    def is_valid_move(original, moved):
        return original != moved

    def count_empty(board):
        return sum(cell == 0 for row in board for cell in row)

    def max_in_corner(board):
        max_tile = max(max(row) for row in board)
        corners = [board[0][0], board[0][3], board[3][0], board[3][3]]
        return max_tile in corners

    def smoothness(board):
        penalty = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    continue
                for dx, dy in ((0, 1), (1, 0)):  # right and down
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj] != 0:
                        diff = abs(math.log2(board[i][j]) - math.log2(board[ni][nj]))
                        penalty += diff
        return -penalty  # negative because it's a penalty

    def monotonicity(board):
        def mono_score(line):
            inc = sum(line[i + 1] - line[i] for i in range(3) if line[i + 1] > line[i])
            dec = sum(line[i] - line[i + 1] for i in range(3) if line[i] > line[i + 1])
            return max(inc, dec) * -1  # want strong trend in one direction
        total = 0
        for row in board:
            total += mono_score(row)
        for col in zip(*board):
            total += mono_score(col)
        return total

    def score_board(board):
        score = 0
        if max_in_corner(board):
            score += 10000
        score += count_empty(board) * 250  # emphasize space
        score += smoothness(board) * 1.5
        score += monotonicity(board) * 1.0
        return score

    directions = {
        'w': move_up,
        'a': move_left,
        's': move_down,
        'd': move_right
    }

    best_score = float('-inf')
    best_move = None

    for dir_key in ['w', 'a', 's', 'd']:
        moved = directions[dir_key](copy.deepcopy(mat))
        if is_valid_move(mat, moved):
            score = score_board(moved)
            if score > best_score:
                best_score = score
                best_move = dir_key

    return best_move if best_move else 'a'

import copy
import math
import random

def AI(mat):
    def compress(row):
        return [num for num in row if num != 0] + [0] * row.count(0)

    def merge(row):
        for i in range(3):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(board):
        new_board = []
        for row in board:
            row = compress(row)
            row = merge(row)
            row = compress(row)
            new_board.append(row)
        return new_board

    def move_right(board):
        return [list(reversed(compress(merge(compress(list(reversed(row))))))) for row in board]

    def transpose(board):
        return [list(row) for row in zip(*board)]

    def move_up(board):
        return transpose(move_left(transpose(board)))

    def move_down(board):
        return transpose(move_right(transpose(board)))
    
    def is_valid_move(original, moved):
        return any(original[i][j] != moved[i][j] for i in range(4) for j in range(4))

    def count_empty(board):
        return sum(cell == 0 for row in board for cell in row)

    def smoothness(board):
        penalty = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    continue
                for dx, dy in ((0, 1), (1, 0)):
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj] != 0:
                        penalty += abs(math.log2(board[i][j]) - math.log2(board[ni][nj]))
        return -penalty

    def monotonicity(board):
        def line_score(line):
            inc = sum(line[i + 1] - line[i] for i in range(3) if line[i + 1] > line[i])
            dec = sum(line[i] - line[i + 1] for i in range(3) if line[i] > line[i + 1])
            return -min(inc, dec)

        total = 0
        for row in board:
            total += line_score(row)
        for col in zip(*board):
            total += line_score(col)
        return total

    def max_in_corner(board):
        max_tile = max(max(row) for row in board)
        corners = [board[0][0], board[0][3], board[3][0], board[3][3]]
        return 1 if max_tile in corners else 0

    def evaluate(board):
        return (
            count_empty(board) * 300 +
            smoothness(board) * 1.5 +
            monotonicity(board) * 1.0 +
            max_in_corner(board) * 10000
        )

    # Movement map
    move_map = {
        'w': move_up,
        'a': move_left,
        's': move_down,
        'd': move_right
    }

    # Expectimax Search
    def expectimax(board, depth, is_player_turn):
        if depth == 0:
            return evaluate(board)

        if is_player_turn:
            max_score = float('-inf')
            for move in move_map:
                new_board = move_map[move](copy.deepcopy(board))
                if is_valid_move(board, new_board):
                    score = expectimax(new_board, depth - 1, False)
                    max_score = max(max_score, score)
            return max_score
        else:
            # AI's turn (tile spawn)
            empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
            if not empty:
                return evaluate(board)
            total = 0
            for (i, j) in empty:
                for value, prob in [(2, 0.9), (4, 0.1)]:
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = value
                    total += prob * expectimax(new_board, depth - 1, True)
            return total / len(empty)

    # Choose best move
    best_score = float('-inf')
    best_move = None
    valid_moves = []
    for move in ['w', 'a', 's', 'd']:
        new_board = move_map[move](copy.deepcopy(mat))
        if is_valid_move(mat, new_board):
            valid_moves.append(move)
            score = expectimax(new_board, depth=2, is_player_turn=False)
            if score > best_score:
                best_score = score
                best_move = move

    return best_move if best_move else random.choice(valid_moves)


import copy
import math
import random

def AI(mat):
    def compress(row):
        return [num for num in row if num != 0] + [0] * row.count(0)

    def merge(row):
        for i in range(3):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(board):
        new_board = []
        for row in board:
            row = compress(row)
            row = merge(row)
            row = compress(row)
            new_board.append(row)
        return new_board

    def move_right(board):
        return [list(reversed(compress(merge(compress(list(reversed(row))))))) for row in board]

    def transpose(board):
        return [list(row) for row in zip(*board)]

    def move_up(board):
        return transpose(move_left(transpose(board)))

    def move_down(board):
        return transpose(move_right(transpose(board)))

    def is_valid_move(original, moved):
        return any(original[i][j] != moved[i][j] for i in range(4) for j in range(4))

    def count_empty(board):
        return sum(cell == 0 for row in board for cell in row)

    def smoothness(board):
        penalty = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    continue
                for dx, dy in ((0, 1), (1, 0)):  # right and down
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj] != 0:
                        penalty += abs(math.log2(board[i][j]) - math.log2(board[ni][nj]))
        return -penalty

    def monotonicity(board):
        def line_score(line):
            inc = sum(line[i + 1] - line[i] for i in range(3) if line[i + 1] > line[i])
            dec = sum(line[i] - line[i + 1] for i in range(3) if line[i] > line[i + 1])
            return -min(inc, dec)

        total = 0
        for row in board:
            total += line_score(row)
        for col in zip(*board):
            total += line_score(col)
        return total

    def max_in_corner(board):
        max_tile = max(max(row) for row in board)
        corners = [board[0][0], board[0][3], board[3][0], board[3][3]]
        return 1 if max_tile in corners else 0

    def evaluate(board):
        # Enhanced evaluation function: prioritize smoothness, empty space, corner control, and larger tiles
        return (
            count_empty(board) * 200 +  # Favor boards with more empty spaces
            smoothness(board) * 1.0 +  # Prioritize smoother boards
            monotonicity(board) * 1.5 +  # Reward monotonic arrangements
            max_in_corner(board) * 5000 +  # Favor boards with larger tiles in corners
            max(max(row) for row in board) * 0.5  # Reward larger tiles
        )

    # Movement map
    move_map = {
        'w': move_up,
        'a': move_left,
        's': move_down,
        'd': move_right
    }

    # Expectimax Search
    def expectimax(board, depth, is_player_turn):
        """Implement expectimax with depth-limited search."""
        if depth == 0:
            return evaluate(board)

        if is_player_turn:
            max_score = float('-inf')
            for move in move_map:
                new_board = move_map[move](copy.deepcopy(board))
                if is_valid_move(board, new_board):
                    score = expectimax(new_board, depth - 1, False)
                    max_score = max(max_score, score)
            return max_score
        else:
            # AI's turn (tile spawn)
            empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
            if not empty:
                return evaluate(board)
            total = 0
            for (i, j) in empty:
                for value, prob in [(2, 0.9), (4, 0.1)]:
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = value
                    total += prob * expectimax(new_board, depth - 1, True)
            return total / len(empty)

    # Choose best move
    best_score = float('-inf')
    best_move = None
    valid_moves = []
    for move in ['w', 'a', 's', 'd']:
        new_board = move_map[move](copy.deepcopy(mat))
        if is_valid_move(mat, new_board):
            valid_moves.append(move)
            score = expectimax(new_board, depth=3, is_player_turn=False)  # Increase depth for better foresight
            if score > best_score:
                best_score = score
                best_move = move

    # If no valid moves are found, return a random move (shouldn't happen often)
    return best_move if best_move else random.choice(valid_moves)


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
# game_logic['AI'] = AI
# gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)
