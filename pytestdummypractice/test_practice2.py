import pytest


def test_login():
    print('login to application')

@pytest.mark.regression
def test_add_cart_and_buy():
    print('add product to the cart and buy it')


def test_logout():
    print('logout from application')