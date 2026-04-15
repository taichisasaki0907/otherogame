from models.board import Board
from models.stone import Stone

def test_reset():
    board = Board()
    assert board.grid[3][3] == Stone.WHITE
    assert board.grid[3][4] == Stone.BLACK
    assert board.grid[4][3] == Stone.BLACK
    assert board.grid[4][4] == Stone.WHITE

def test_display(capsys):
    board = Board()
    board.display()
    output = capsys.readouterr().out
    assert "0 1 2 3 4 5 6 7" in output
    assert "3 . . . W B . . ." in output
    assert "4 . . . B W . . ." in output

def test_on_board():
    board = Board()
    assert board.on_board(0, 0) is True
    assert board.on_board(7, 7) is True
    assert board.on_board(-1, 0) is False
    assert board.on_board(0, -1) is False
    assert board.on_board(8, 0) is False
    assert board.on_board(0, 8) is False
    
def test_get_flippable_stones():
    board = Board()
    assert board.get_flippable_stones(-1, 0, Stone.BLACK) == []
    assert board.get_flippable_stones(3, 3, Stone.BLACK) == []
    assert board.get_flippable_stones(0, 0, Stone.BLACK) == []

def test_get_flippable_stones_con():
    board = Board()
    board.set_cell(1, 0, Stone.WHITE)
    board.set_cell(2, 0, Stone.WHITE)
    board.set_cell(3, 0, Stone.WHITE)
    
    assert board.get_flippable_stones(4, 0, Stone.BLACK) == []
    board.set_cell(0, 0, Stone.WHITE)
    assert board.get_flippable_stones(4, 0, Stone.BLACK) == []
    board.set_cell(0, 0, Stone.BLACK)
    assert board.get_flippable_stones(4, 0, Stone.BLACK) == [(3, 0), (2, 0), (1, 0)]

def test_is_placeable():
    board = Board()
    assert board.is_placeable(2, 3, Stone.BLACK) is True 
    assert board.is_placeable(7, 7, Stone.BLACK) is False

def test_place_stone():
    board = Board()
    assert board.place_stone(2, 3, Stone.BLACK) is True
    assert board.grid[3][2] == Stone.BLACK
    assert board.grid[3][3] == Stone.BLACK

def test_get_placeable_cells():
    board = Board()
    assert board.get_placeable_cells(Stone.BLACK) == [(3, 2), (2, 3), (5, 4), (4, 5)]