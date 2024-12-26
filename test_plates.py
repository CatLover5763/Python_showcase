from plates import is_valid


def test_is_valid():
    assert is_valid("123456") == False
    assert is_valid("baldur's gate 3") == False
    assert is_valid("") == False
    assert is_valid("CS.50") == False
    assert is_valid("AAA22A") == False
    assert is_valid("KKK963") == True
    assert is_valid("CS05") == False
