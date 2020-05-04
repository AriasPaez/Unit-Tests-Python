import unittest
from shopping_cart import Item

class TestShoppingCart(unittest.TestCase):

    def test_product_name_equal_to_apple(self):
        item = Item('Apple', 700)
        self.assertEqual(item.name, 'Apple')

    def test_product_name_different_to_apple(self):
        item = Item('Coco', 500)
        self.assertNotEqual(item.name, 'Apple')
        

if __name__=='__main__':
    unittest.main()