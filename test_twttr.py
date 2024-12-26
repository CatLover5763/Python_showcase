from twttr import shorten


def test_shorten():
    assert shorten("Cat") == "Ct"
    assert shorten("Twitter") == "Twttr"
    assert shorten("brb.") == "brb."
    assert shorten("AAAAAAAAAAAAAA") == ""
    assert shorten("Max_payne") == "Mx_pyn"
    assert shorten("Alan wake") == "ln wk"
    assert shorten("baldur's gate 3") == "bldr's gt 3"
