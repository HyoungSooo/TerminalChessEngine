from board.stock_fish import StockFishEngine as sf
from board.chessboard import Board as cb


def battle(board: cb, start_white: bool = True):

    engine = board.stockfish
    engine.get_board_visual(start_white, False)
    while True:
        level = input("Enter level(must be int) 1 ~ 20 : ")
        try:
            if 1 <= int(level) <= 20:
                engine.set_skill_level(level)
                break
        except:
            print("Invalid level")

    if not start_white:
        move = engine.get_best_move()
        engine.move_piece([move])
        board.board.push_san(move)
        engine.get_board_visual(start_white, False)

    while True:
        move = input(
            "1) enter move, 2) evaluation, 3) get best moves(count : 3), 4) exit (enter only number (ex : 3)) : "
        )

        if move == "1":
            legal = [str(legal_move) for legal_move in board.board.legal_moves]
            print(legal)
            while True:
                move = input("Enter move : ")
                if move in legal:
                    break
            engine.move_piece([move])
            board.board.push_san(move)

            if board.board.is_game_over():
                print("game over")
                break

            engine.get_board_visual(start_white, False)
            sf_move = engine.get_best_move()
            engine.move_piece([sf_move])
            board.board.push_san(sf_move)
            print(f"sf moves : {sf_move}")
            engine.get_board_visual(start_white, False)

            if board.board.is_game_over():
                print("game over")
                break
        elif move == "2":
            print(engine.get_evaluation())
        elif move == "3":
            print(engine.engine.get_top_moves(3))
        elif move == "4":
            break

        if board.board.is_game_over():
            print("game over")
            break
