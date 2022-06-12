import unittest
from product import Product
from product import ProductDiscountError
from shopping_cart import ShoppingCart



from product import Product

def is_available_to_skip():
    return False

def is_conected():
    return False

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
    
    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name= 'Example', price= 10.0, discount= 11.0)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_products(Product(name = 'Libro', price = 15.0))
        self.shopping_cart_1.add_products(Product(name = 'Camera', price = 700.0, discount = 70))
        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 1000)
        self.assertEqual(self.shopping_cart_1.total, 645.00)
        #assertGreaterEqual
        #assertLessEqual

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total,0)
        
    @unittest.skip('Just because, jiji, the test does not comply :(')
    def test_skip_example(self):
        self.assertEqual(1,1)

    # skipIf -> evaluate True
    # skipunless -> evaluate False

    @unittest.skipIf(is_available_to_skip(),'Just because, it dont count with all the requerimet')
    def test_skip_exampple_two(self):
        pass

    @unittest.skipUnless(is_conected(),'Just because, it dont count with all the requerimet')
    def test_skip_exampple_two(self): 
        pass

    def test_code_product(self):
        self.assertRegex(self.smartphone.code,self.smartphone.name) #regex
        
if __name__ == '__main__':
    unittest.main()
