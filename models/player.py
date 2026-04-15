from typing import Protocol
from .stone import Stone
from .board import Board
import random


class PlayerProtocol(Protocol):
    name: str
    stone: Stone

    def choose_move(self, board: Board) -> tuple[int, int]:
        ...

class HumanPlayer:
    def __init__(self, name: str, stone: Stone):
        self.name = name
        self.stone = stone

    def choose_move(self, board: Board) -> tuple[int, int]:
        while True:
            try:
                x = int(input("x: "))
                y = int(input("y: "))
                return x, y
            except ValueError:
                print("整数を入力してください")

class CPUPlayer:
    def __init__(self, name: str, stone: Stone):
        self.name = name
        self.stone = stone

    def choose_move(self, board: Board) -> tuple[int, int]:
        placeable_cells = board.get_placeable_cells(self.stone)
        return random.choice(placeable_cells)


