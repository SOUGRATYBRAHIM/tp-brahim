from src.app import add

def test_add():
    assert add(3,1) == 4
    
def test_moin():
    assert add(3,-1) == 2
    

