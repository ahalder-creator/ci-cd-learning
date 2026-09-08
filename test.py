from app import add
def test_add():
    assert add(2, 3) == 5

def test_add_wrong():
    assert add(2, 3) == 6
