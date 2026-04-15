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
    for y in range(game.board.size):
        for x in range(game.board.size):
            game.board.set_cell(x, y, Stone.BLACK)
    assert game.is_game_over() is True


def test_display_result_black_win(capsys):
    game = Game()
    for y in range(game.board.size):
        for x in range(game.board.size):
            game.board.set_cell(x, y, Stone.BLACK)
    game.display_result()
    output = capsys.readouterr().out
    assert "黒の得点: 64" in output
    assert "白の得点: 0" in output
    assert "黒の勝ち" in output

def test_display_result_white_win(capsys):
    game = Game()
    for y in range(game.board.size):
        for x in range(game.board.size):
            game.board.set_cell(x, y, Stone.WHITE)
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


