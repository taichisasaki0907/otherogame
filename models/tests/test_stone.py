from models.stone import Stone

def test_stone_values():
    assert Stone.WHITE == -1
    assert Stone.EMPTY == 0
    assert Stone.BLACK == 1

def test_stone_values_reverse():
    assert -Stone.WHiTE == Stone.BLACK == 1
    assert -Stone.EMPTY == Stone.EMPTY == 0
    assert -Stone.BLACK == Stone.WHITE == -1


