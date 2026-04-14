from models.stone import Stone
from models.game import Game

def test_switch_turn():
    game = Game()
    assert game.turn == Stone.BLACK
    game.switch_turn()
    assert game.turn == Stone.WHITE

def test_is_game_over():
    game = Game()
    assert game.is_game_over() is False
    game.board.grid = [[Stone.BLACK for _ in range(game.board.size)] for _ in range(game.board.size)]
    assert game.is_game_over() is True


def test_display_result_black_win(capsys):
    game = Game()
    game.board.grid = [[Stone.BLACK for _ in range(game.board.size)] for _ in range(game.board.size)]
    game.display_result()
    output = capsys.readouterr().out
    assert "黒の得点: 64" in output
    assert "白の得点: 0" in output
    assert "黒の勝ち" in output

def test_display_result_white_win(capsys):
    game = Game()
    game.board.grid = [[Stone.WHITE for _ in range(game.board.size)] for _ in range(game.board.size)]
    game.display_result()
    output = capsys.readouterr().out
    assert "黒の得点: 0" in output
    assert "白の得点: 64" in output
    assert "白の勝ち" in output

def test_display_result_draw(capsys):
    game = Game()
    game.display_result()
    output = capsys.readouterr().out
    assert "黒の得点: 2" in output
    assert "白の得点: 2" in output
    assert "引き分け" in output

def test_get_random_cpu_move():
    game = Game()
    game.turn = Stone.WHITE

    move = game.get_random_cpu_move()

    assert move in [(4, 2), (5, 3), (2, 4), (3, 5)]
