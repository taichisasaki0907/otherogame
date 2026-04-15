from .board import Board
from .stone import Stone
from .player import PlayerProtocol, HumanPlayer, CPUPlayer

#クラス：ゲーム
class Game:
  def __init__(self) -> None:
    self.board = Board()
    self.turn = Stone.BLACK
    self.black_player = None
    self.white_player = None
  # 黒プレイヤーを選ぶ
  def select_black_player(self) -> PlayerProtocol:
    while True:
      print("プレイヤー(黒)を選んでください。1: プレイヤー 2: CPU")
      choice = input()

      if choice == "1":
          return HumanPlayer("Player1", Stone.BLACK)
      elif choice == "2":
          return CPUPlayer("CPU(黒)", Stone.BLACK)
      else:
          print("1 か 2 を入力してください")

  # 白プレイヤーを選ぶ
  def select_white_player(self) -> PlayerProtocol:
    while True:
      print("プレイヤー(白)を選んでください。1: プレイヤー 2: CPU")
      choice = input()

      if choice == "1":
          return HumanPlayer("Player2", Stone.WHITE)
      elif choice == "2":
          return CPUPlayer("CPU(白)", Stone.WHITE)
      else:
          print("1 か 2 を入力してください")           


  # ターンを交代
  def switch_turn(self) -> None:
    self.turn = self.turn.flip_stone()

  # 現在のプレイヤー
  def get_current_player(self) -> PlayerProtocol:
    if self.turn == Stone.BLACK:
        return self.black_player
    return self.white_player

  # ゲーム終了
  def is_game_over(self) -> bool:
    return (
        len(self.board.get_placeable_cells(self.turn)) == 0
        and len(self.board.get_placeable_cells(self.turn.flip_stone())) == 0
    )

  # ゲーム進行
  def play(self) -> None:

    self.black_player = self.select_black_player()
    self.white_player = self.select_white_player()
    # ゲームが続いてる限り進行
    while not self.is_game_over():

      # コマを置ける場所がなかったらターンを交代
      if len(self.board.get_placeable_cells(self.turn)) == 0:
        print("パス")
        self.switch_turn()
        continue

      # 現在の盤面を表示
      self.board.display()

      # 現在のターンを表示
      if self.turn == Stone.BLACK:
        print("黒のターン")
      else:
        print("白のターン")

      # コマをおける座標を表示
      print(f"置ける場所: {self.board.get_placeable_cells(self.turn)}")

      # 現在のプレイヤー
      current_player = self.get_current_player()

      while True:
        # プレイヤーの手を取得
        x, y = current_player.choose_move(self.board)

        if self.board.place_stone(x, y, self.turn):
            print(f"({x}, {y})に置いた")
            self.switch_turn()
            break
        else:
            print("そこには置けない")
      

    self.board.display()
    self.display_result()


  # 試合結果を表示
  def display_result(self) -> None:
    score_black = 0
    score_white = 0
    for i in range(self.board.size):
      for j in range(self.board.size):
        if self.board.grid[i][j] == Stone.BLACK:
          score_black += 1
        elif self.board.grid[i][j] == Stone.WHITE:
          score_white += 1

    print(f"黒の得点: {score_black}")
    print(f"白の得点: {score_white}")

    if score_black > score_white:
      print("黒の勝ち")
    elif score_black < score_white:
      print("白の勝ち")
    else:
      print("引き分け")

  



