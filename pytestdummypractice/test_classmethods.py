import pytest

@pytest.mark.usefixtures('setup')
class Testmethods:

    def test_pay_electricity_bill(self):
        print('This is a important functionality')
        print('Enter the Id and pay the bill')

    def test_add_new_customer(self):
        print('This is one of the key functionality')
        print('select add customer tab, enter the details and add the customer')

    def test_update_customers_aadhar_card(self):
        print("enter customer's name or Id")
        print('Select aadharcard tab and upload the document')

    def test_login(self):
        print('login to application')

    def test_add_cart_and_buy(self):
        print('add product to the cart and buy it')

    def test_logout(self):
        print('logout from application')

