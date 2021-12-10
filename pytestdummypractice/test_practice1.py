import pytest

def test_print():
    print('this is a demo practice test')


def test_compare():
    x = 10
    y = 20
    assert x == y, 'The numbers do not match'

@pytest.mark.regression
def test_stringcompare():
    x = 'Selenium'
    y = 'Selenium is a package which helps in automating web'
    assert x in y, 'The given string is not in the title'





