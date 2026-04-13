import random
# コマを定義
WHITE = -1
EMPTY = 0
BLACK = 1

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

class Board:
    def __init__(self):
      self.size = 8
      self.grid = [[EMPTY for _ in range(self.size)] for _ in range(self.size)]
      self.reset()

    # 初期配置
    def reset(self):
      self.grid[3][3] = WHITE
      self.grid[3][4] = BLACK
      self.grid[4][3] = BLACK
      self.grid[4][4] = WHITE

    # 表示
    def display(self):
      print("  ", end="")
      for x in range(self.size):
          print(x, end=" ")
      print()
      for y in range(self.size):
          print(y, end=" ")
          for x in range(self.size):
            if self.grid[y][x] == WHITE:
              print("W", end=" ")
            elif self.grid[y][x] == BLACK:
              print("B", end=" ")
            else:
              print(".", end=" ")
          print()


    # 盤上か
    def on_board(self, x, y):
      return 0 <= x < self.size and 0 <= y < self.size

    # 置いた時に返せるコマのリストを取得
    def get_flippable_stones(self, x, y, stone):

      # 盤上でなければ失敗
      if not self.on_board(x, y):
        return []

      # 空マスでなければ失敗
      if self.grid[y][x] != EMPTY:
        return []

      #隣接方向に相手のコマがあり、その先に自分のコマがあるか

      enemy_stone = -stone #相手のコマ

      flippable_stones = [] # 返せるコマを格納

      # 8方向を探索する
      for dx, dy in DIRECTIONS:
        nx = x + dx
        ny = y + dy

        # 探索方向が盤外ならこの方向を探索終了
        if not self.on_board(nx, ny):
          continue

        # 探索方向が相手のコマでなければこの方向を探索終了
        if self.grid[ny][nx] != enemy_stone:
          continue

        # この方向で返せる可能性のあるコマを一時格納
        temp_flippable_stones = []

        # 相手のコマが続く限りその方向を探索
        while self.on_board(nx, ny) and self.grid[ny][nx] == enemy_stone:
          temp_flippable_stones.append((nx, ny))
          nx += dx
          ny += dy

        # 盤外に出たらこの方向を探索終了
        if not self.on_board(nx, ny):
          continue

        # 空マスに当たったらこの方向を探索終了

        # 自分のコマに当たったら探索成功
        if self.grid[ny][nx] == stone:
          flippable_stones.extend(temp_flippable_stones)

      # 完走
      return flippable_stones

    # コマを置けるかを判定
    def is_placeable(self, x, y, stone):
      return len(self.get_flippable_stones(x, y, stone)) > 0

    # コマ置いてひっくり返す
    def place_stone(self, x, y, stone):
      flippable_stones = self.get_flippable_stones(x, y, stone)

      # 返せるコマがなければ失敗
      if len(flippable_stones) == 0:
        return False

      # コマを置く
      self.grid[y][x] = stone

      # 返せるコマを全て反転
      for fx, fy in flippable_stones:
        self.grid[fy][fx] *= -1
      return True

    # コマを置ける座標を取得
    def get_placeable_cells(self, stone):
      placeable_cells = []
      for y in range(self.size):
        for x in range(self.size):
          if self.is_placeable(x, y, stone):
            placeable_cells.append((x, y))
      return placeable_cells

#クラス：ゲーム
class Game:
  def __init__(self):
    self.board = Board()
    self.turn = BLACK

  # ターンを交代
  def switch_turn(self):
    self.turn *= -1

  # ゲーム終了
  def is_game_over(self):
    return (
        len(self.board.get_placeable_cells(self.turn)) == 0
        and len(self.board.get_placeable_cells(-self.turn)) == 0
    )

  # ゲーム進行
  def play(self):
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
      if self.turn == BLACK:
        print("黒のターン")
      else:
        print("白のターン")

      # コマをおける座標を表示
      print(f"置ける場所: {self.board.get_placeable_cells(self.turn)}")

      # CPUのターンならランダムにコマを置く
      if self.turn == WHITE:
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
  def display_result(self):
    score_black = 0
    score_white = 0
    for i in range(self.board.size):
      for j in range(self.board.size):
        if self.board.grid[i][j] == BLACK:
          score_black += 1
        elif self.board.grid[i][j] == WHITE:
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
  def get_random_cpu_move(self):
    placeable_cells = self.board.get_placeable_cells(self.turn)
    if len(placeable_cells) == 0:
      return None
    return random.choice(placeable_cells)



