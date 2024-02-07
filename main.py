import chess
from board.chessboard import Board as cb
from board.stock_fish import StockFishEngine as sf
from board.mode.battle_stockfish import battle


def main():
    board = cb("./board/stockfish-16-mac/bin/stockfish")

    print("1) Start puzzle, 2) Battle with stockfish 3) exit")
    mode = input("Enter mode : ")

    if mode == "1":
        board.start_puzzle()
        main()
    elif mode == "2":
        battle(board, True)
        main()
    else:
        return


if __name__ == "__main__":
    main()
