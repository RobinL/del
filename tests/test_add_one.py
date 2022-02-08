from my_functions import add_one


def test_add_one():
    expected = 2
    actual = add_one(1)
    assert expected == actual


def test_add_one_again():
    expected = 3
    actual = add_one(2)
    assert expected == actual