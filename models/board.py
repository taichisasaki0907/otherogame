from .stone import Stone, DIRECTIONS

class Board:
    def __init__(self) -> None:
      self.size = 8
      self.grid = [[Stone.EMPTY for _ in range(self.size)] for _ in range(self.size)]
      self.reset()

    # 初期配置
    def reset(self) -> None:
      self.grid[3][3] = Stone.WHITE
      self.grid[3][4] = Stone.BLACK
      self.grid[4][3] = Stone.BLACK
      self.grid[4][4] = Stone.WHITE

    # 表示
    def display(self) -> None:
      print("  ", end="")
      for x in range(self.size):
          print(x, end=" ")
      print()
      for y in range(self.size):
          print(y, end=" ")
          for x in range(self.size):
            if self.grid[y][x] == Stone.WHITE:
              print("W", end=" ")
            elif self.grid[y][x] == Stone.BLACK:
              print("B", end=" ")
            else:
              print(".", end=" ")
          print()


    # 盤上か
    def on_board(self, x: int, y: int) -> bool:
      return 0 <= x < self.size and 0 <= y < self.size

    # 置いた時に返せるコマのリストを取得
    def get_flippable_stones(self, x: int, y: int, stone: Stone) -> list[tuple[int, int]]:

      # 盤上でなければ失敗
      if not self.on_board(x, y):
        return []

      # 空マスでなければ失敗
      if self.grid[y][x] != Stone.EMPTY:
        return []

      #隣接方向に相手のコマがあり、その先に自分のコマがあるか

      enemy_stone = stone.flip_stone() #相手のコマ

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
    def is_placeable(self, x: int, y: int, stone: Stone) -> bool:
      return len(self.get_flippable_stones(x, y, stone)) > 0

    # コマ置いてひっくり返す
    def place_stone(self, x: int, y: int, stone: Stone) -> bool:
      flippable_stones = self.get_flippable_stones(x, y, stone)

      # 返せるコマがなければ失敗
      if len(flippable_stones) == 0:
        return False

      # コマを置く
      self.grid[y][x] = stone

      # 返せるコマを全て反転
      for fx, fy in flippable_stones:
        self.grid[fy][fx] = self.grid[fy][fx].flip_stone()
      return True

    # コマを置ける座標を取得
    def get_placeable_cells(self, stone: Stone) -> list[tuple[int, int]]:
      placeable_cells = []
      for y in range(self.size):
        for x in range(self.size):
          if self.is_placeable(x, y, stone):
            placeable_cells.append((x, y))
      return placeable_cells
