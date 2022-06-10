import unittest 
from product import Product

class shoppingCart(unittest.TestCase):

    def test_product_object(self):
        name = 'apple'
        price = 1.70

        product = Product(name,price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, 10.0, 'We sorry the price is not the same')


if __name__ == '__main__':
    unittest.main()
