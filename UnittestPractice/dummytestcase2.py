import unittest

class apptesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print('this is login test')

    @classmethod
    def tearDown(self):
        print('this is logout test')

    @classmethod
    def setUpClass(cls):
        print('opening application')

    @classmethod
    def tearDownClass(cls):
        print('closing the application')

    def test_search(self):
        print('this is search test')

    def test_advsearch(self):
        print('this is advanced search')

    def test_prepaid(self):
        print('this is prepaid recharge test')

    def test_postpaid(self):
        print('thhis is postpaid recharge test')

if __name__ == "__main__":
    unittest.main()