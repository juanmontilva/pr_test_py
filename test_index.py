from index import suma

def test_compare_sum():
    r = suma()
    token = False
    if r == 2:
        token = True
    assert token == True
