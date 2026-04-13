import random

from .board import Board
from .stone import Stone


#クラス：ゲーム
class Game:
  def __init__(self) -> None:
    self.board = Board()
    self.turn = Stone.BLACK

  # ターンを交代
  def switch_turn(self) -> None:
    self.turn *= -1

  # ゲーム終了
  def is_game_over(self) -> bool:
    return (
        len(self.board.get_placeable_cells(self.turn)) == 0
        and len(self.board.get_placeable_cells(-self.turn)) == 0
    )

  # ゲーム進行
  def play(self) -> None:
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

      # CPUのターンならランダムにコマを置く
      if self.turn == Stone.WHITE:
        move = self.get_random_cpu_move()

        if move is not None:
          x, y = move
          self.board.place_stone(x, y, self.turn)
          print(f"CPUは ({x}, {y}) に置いた")
          self.switch_turn()
          continue

      # コマを置かせる
      try:
        x = int(input("x: "))
        y = int(input("y: "))
      except ValueError:
        print("整数を入力してください")
        continue

      if self.board.place_stone(x, y, self.turn):
        self.switch_turn()
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

  # ランダムに次の手を決める(CPU)
  def get_random_cpu_move(self) -> tuple[int, int] | None:
    placeable_cells = self.board.get_placeable_cells(self.turn)
    if len(placeable_cells) == 0:
      return None
    return random.choice(placeable_cells)



