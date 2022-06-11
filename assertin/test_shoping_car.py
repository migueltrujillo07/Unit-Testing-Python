import unittest
from product import Product
from shopping_cart import ShoppingCart


from product import Product

class TestShoppingCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('>>> Method class setUp excute before all the test')
    @classmethod
    def tearDownClass(cls):
        print('>>> Method class TearDown excute after all the test')



    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_products(self.smartphone)

    def tearDown(self):
        pass
        #print('>>> El método tearDown se ejecuta despues de cada una de las pruebas.')

    def test_product_object(self):
        pass
    
    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)


    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'So sorry but the shopping car is not empty')

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())


    def test_product_in_shopping_cart(self):
                
        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_products(product)

        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)


    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)

        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

if __name__ == '__main__':
    unittest.main()
