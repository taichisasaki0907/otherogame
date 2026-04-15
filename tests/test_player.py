from models.player import PlayerProtocol, HumanPlayer, CPUPlayer
from models.board import Board
from models.stone import Stone

def test_cpu_move():
    board = Board()
    cpu = CPUPlayer("CPU", Stone.BLACK)

    cpu_move = cpu.choose_move(board)
    assert cpu_move in board.get_placeable_cells(cpu.stone)