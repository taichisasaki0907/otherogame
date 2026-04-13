from enum import IntEnum


class Stone(IntEnum):
    WHITE = -1
    EMPTY = 0
    BLACK = 1


DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]