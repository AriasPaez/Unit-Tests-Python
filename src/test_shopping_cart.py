import unittest
from shopping_cart import ShoppingCart, NotExistsItemError
from item import Item

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.carrot = Item('Carrot', 900)
        self.strawberry = Item('Strawberry', 500)
        self.apple = Item('Apple', 700)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.strawberry)
    
    def tearDown(self):
        pass

    def test_product_name_equal_to_apple(self):         #==
        value_to_test = 'Apple'
        self.assertEqual(self.apple.name, value_to_test, 'Falló: {} no es igual a {}'.format(self.apple.name, value_to_test))

    def test_product_name_different_to_apple(self):
        self.assertNotEqual(self.carrot.name, 'Apple')

    def test_shopping_cart_contains_some_item(self):
        self.assertTrue(self.shopping_cart.contains_items())
    
    def test_shopping_cart_not_contains_any_item(self):
        self.shopping_cart.clear_items()
        self.assertFalse(self.shopping_cart.contains_items())
    
    def test_get_item_strawberry(self): # is
        item = self.shopping_cart.get_item(self.strawberry)
        self.assertIs(item, self.strawberry)

    def test_exception_to_get_item(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.carrot)
    
    def test_total_items(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertLess(total, self.carrot.price)

    def test_code_carrot(self):
        
        self.assertRegex(self.carrot.code(), self.carrot.name)


    @unittest.skip("Motivo de skip") #Cuando conocemos que la prueba no puede ejecutarse
    def test_skip(self):
        pass


    @unittest.skipIf(False, 'Motivo por el que se omite')#Cuando desconocemos si la prueba puede o no ejecutarse, a causa de motivos externos
    def test_skip_if(self):
        pass
if __name__=='__main__':
    unittest.main()