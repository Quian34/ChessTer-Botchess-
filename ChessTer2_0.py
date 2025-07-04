# importaciones
import chess
import numpy 
from chess import Board


#Tablero de ajedrez trabajado en una matriz
def board_matrix(board: Board):
    matrix = numpy.zeros((13, 8, 8))
    piece_map = board.piece_map()
    #Matríz 8 x 8, 12 piezas únicas y 13 es el tablero para jugadas legales

#Donde están las piezas
    for square, piece in piece_map.items():
        row, col = divmod(square, 8)
        piece_type = piece.piece_type -1
        piece_color = 0 if piece.color else 6 #Blanca 0-5 / Negras 6-11
        matrix[piece_type + piece_color, row, col] = 1

#Jugadas legales
legal_moves = board.legal_moves
for move in legal_moves:
    to_square = move.to_square
    row_to, col_to = divmod(to_square, 8)
    matrix[12, row_to, col_to] = 1

return matrix

def input_nn(games):
    x = []
    y = []
    for game in games:
        board = game.board()
        for move in game.mainline_moves():
            x.append(board_matrix(board))
            y.append(move.uci())
            board.push(move)
    return numpy.array(x, dtype=numpy.float32), numpy.array(y)

def encode(moves):
    move_init = {move: idx for idx, move in enumerate(set(moves))}
    return numpy.array([move_init[move] for move in moves], dtype=numpy.float32), move_init


