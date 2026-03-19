pip install python-shogi
import shogi

def print_board(board: shogi.Board):
    # python-shogi の __str__ をそのまま使う
    print(board)
    print()
    print("手番:", "先手" if board.turn == shogi.BLACK else "後手")
    print("持ち駒（先手）:", board.pieces_in_hand[shogi.BLACK])
    print("持ち駒（後手）:", board.pieces_in_hand[shogi.WHITE])
    print("-" * 40)

def main():
    board = shogi.Board()
    print("=== Python 将棋 ===")
    print("指し手は USI 形式で入力してください（例: 7g7f, 8h2b+, B*5e など）")
    print("終了したいときは 'quit' を入力")
    print_board(board)

    while True:
        if board.is_game_over():
            print("対局終了:", board.result())
            if board.is_checkmate():
                print("詰みです。", "先手の勝ち" if board.turn == shogi.WHITE else "後手の勝ち")
            elif board.is_stalemate():
                print("ステイルメイト")
            elif board.is_repetition():
                print("千日手")
            elif board.is_insufficient_material():
                print("持将棋（駒不足）")
            break

        # 手番表示
        side = "先手" if board.turn == shogi.BLACK else "後手"
        move_str = input(f"{side}の手を入力してください (USI): ").strip()

        if move_str.lower() in ("quit", "exit"):
            print("対局を中断しました。")
            break

        try:
            # USI 文字列から Move を生成
            move = shogi.Move.from_usi(move_str)
        except ValueError:
            print("USI 形式が不正です。例: 7g7f, 8h2b+, B*5e")
            continue

        # 合法手かどうかチェック
        if move not in board.legal_moves:
            print("その手は合法手ではありません。もう一度入力してください。")
            continue

        # 指す
        board.push(move)
        print_board(board)

if __name__ == "__main__":
    main()
