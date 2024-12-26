from bank import value


def test_value():
    assert value("Hello") == 0
    assert value("hi") == 20
    assert value("Chalee roy") == 100
    assert value("123") == 100
