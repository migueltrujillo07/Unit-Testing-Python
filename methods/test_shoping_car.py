import unittest

from product import Product

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)

    def tearDown(self):
        pass
        #print('>>> El método tearDown se ejecuta despues de cada una de las pruebas.')

    def test_product_object(self):
        pass
    
    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)



if __name__ == '__main__':
    unittest.main()
