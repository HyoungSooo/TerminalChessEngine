import chess
from board.stock_fish import StockFishEngine as sf
from board.puzzle.puzzle_client import PuzzleClient as pc
from collections import deque


class Board:
    def __init__(self, path):
        self.board = chess.Board()

        self.client = pc()
        self.stockfish = sf(path)

    def start_puzzle(self):
        puzzle = self.client.get_puzzle()

        self.stockfish.set_fen_position(puzzle.get("fen"))
        turn = self.stockfish.engine.get_fen_position().split(" ")[1]

        moves = deque(puzzle.get("move"))

        while moves:
            print(f"\ncomputer moves  :  {moves[0]}")
            self.stockfish.move_piece([moves.popleft()])
            if turn == "w":
                self.stockfish.get_board_visual(False)
            else:
                self.stockfish.get_board_visual()
            while True:
                move = input("Enter move : ")
                if move == moves[0]:
                    self.stockfish.move_piece([moves.popleft()])
                    break
                else:
                    print("Wrong move")

            if not moves:
                print("Puzzle complete")
                break

        retry = input("Next? (y/n) : ")
        if retry == "y":
            self.start_puzzle()
        else:
            return
