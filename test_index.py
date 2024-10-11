from index import suma, resta

def test_compare_sum():
    r = suma()
    token = False
    if r == 2:
        token = True
    assert token == True

def test_compare_subtract():
    r = restar()
    token = False
    if r == 1:
        token = True
    
    res = isinstance(r, int)
    assert(r, int, token) == (res, int, True)
