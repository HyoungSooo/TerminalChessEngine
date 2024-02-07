from stockfish import Stockfish


class StockFishEngine:
    def __init__(
        self,
        path,
        depth=20,
    ):
        self.engine = Stockfish(path=path)
        self.engine.set_depth(depth)
        self.engine.set_skill_level(20)

    def get_best_move(self):
        return self.engine.get_best_move()

    def move_piece(self, moves):
        self.engine.make_moves_from_current_position(moves)

    def set_fen_position(self, fen):
        if self.engine.is_fen_valid(fen):
            self.engine.set_fen_position(fen)
        else:
            print("Invalid FEN")

        self.get_board_visual()

    def get_evaluation(self):
        return self.engine.get_evaluation()

    def get_board_visual(self, white=True):
        print(self.engine.get_board_visual(white))
        return self.engine.get_board_visual()

    def set_skill_level(self, level):
        self.engine.set_skill_level(level)
