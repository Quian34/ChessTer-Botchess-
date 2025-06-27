import chess


#Fundamentos necesarios para min max
class Motor:
        def __init__(self, color):
            self.color = color
        # color debe ser chess.WHITE o chess.BLACK
        # Devuelve True si es el turno del motor según el color que controla
        def es_mi_turno(self, board):
            return board.turn == self.color
        def jugar_turno(self, board):
            if board.turn == self.color:
                self.board = board  # asignar para que min_max pueda usarlo
                move = self.elegir_mejor_jugada(depth=3)  # o la profundidad que quieras
                if move:
                    board.push(move)
                    print(move)
#Arbol minmax
        def min_max(self, depth, maximizing_player):
            if depth == 0 or self.board.is_game_over():
                return self.eval_place()
            if maximizing_player:
        #Arbol max
                max_eval = float("-inf")
                for move in self.board.legal_moves:
                    self.board.push(move)
                    eval = self.min_max(depth -1, False)
                    self.board.pop()
                    max_eval = max(max_eval, eval)
                    return max_eval
            else:
            #Arbol min
                min_eval = float("inf")
                for move in self.board.legal_moves:
                    self.board.push(move)
                    eval = self.min_max(depth -1, True)
                    self.board.pop()
                    min_eval = min(min_eval, eval)
                    return min_eval

#Función de evaluar posición
        def eval_place(self):
        # Evaluación simple: +1 por cada pieza propia, -1 por cada pieza rival
        # Puedes mejorar esta función con heurísticas más avanzadas
            value = 0
            piezas_value = {
                chess.PAWN: 1,
                chess.KNIGHT: 3,
                chess.BISHOP: 3,
                chess.ROOK: 5,
                chess.QUEEN: 9,
                chess.KING: 0
        }
            for square in chess.SQUARES:
                pieza = self.board.piece_at(square)
                if pieza:
                    value_pieza = piezas_value.get(pieza.piece_type, 0)
                    if pieza.color == self.color:
                        value += value_pieza
                    else:
                        value -= value_pieza
            return value

        def elegir_mejor_jugada(self, depth):
            mejor_value = float("-inf") if self.color == chess.WHITE else float("inf")
            mejor_jugada = None
            
            for move in self.board.legal_moves:
                self.board.push(move)
                value = self.min_max(depth - 1, self.color != chess.WHITE)
                self.board.pop()
                print(f"Move: {move}, Value: {value}")  # Debug

                if value is None:
                    print("Error: min_max devolvió None")
                    continue  # evitar comparar con None

            if self.color == chess.WHITE:
                if value > mejor_value:
                    mejor_value = value
                    mejor_jugada = move
            else:
                if value < mejor_value:
                    mejor_value = value
                    mejor_jugada = move
            return mejor_jugada


def elegir_color_user():
    eleccion = input("Elige color (blancas/negras): ").strip().lower()
    if eleccion == "blancas":
        return chess.WHITE
    elif eleccion == "negras":
        return chess.BLACK
    else:
        print("Opción no válida, se asignan blancas por defecto.")
        return chess.WHITE


if __name__ == "__main__":
    color_usuario = elegir_color_user()
    motor = Motor(chess.BLACK if color_usuario == chess.WHITE else chess.WHITE)
    board = chess.Board()
    # Ejemplo simple de loop de juego
    while not board.is_game_over():
        if board.turn == color_usuario:
            # Aquí iría la jugada del usuario (input o interfaz)
            print(board)
            jugada = input("Tu jugada (en notación SAN): ")
            try:
                move = board.parse_san(jugada)
                board.push(move)
            except:
                print("Movimiento inválido, intenta de nuevo.")
        else:
            motor.jugar_turno(board)

    print("Partida terminada:", board.result())

