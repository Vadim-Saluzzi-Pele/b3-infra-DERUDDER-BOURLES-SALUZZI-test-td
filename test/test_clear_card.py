import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def setUp(self):
        """Initialisation d'un panier avec des produits pour chaque test."""
        self.cart = Cart()
        self.product1 = Product(name="Laptop", price=1200.0, stock=5)
        self.product2 = Product(name="Headphones", price=150.0, stock=10)
        # Ajouter des produits au panier
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 3)

    def test_clear_cart(self):
        """Tester que la méthode clear_cart vide correctement le panier."""
        # Vérification avant de vider le panier
        self.assertGreater(len(self.cart.items), 0, "Cart should not be empty before clearing.")
        
        # Appel de la méthode clear_cart
        result = self.cart.clear_cart()
        
        # Vérification après avoir vidé le panier
        self.assertEqual(len(self.cart.items), 0, "Cart should be empty after calling clear_cart.")
        self.assertEqual(result, "Cart has been cleared.", "Return message should confirm clearing.")
        
    def test_clear_cart_on_empty_cart(self):
        """Tester que la méthode clear_cart fonctionne même si le panier est déjà vide."""
        # Vider le panier une première fois
        self.cart.clear_cart()
        
        # Appel de la méthode clear_cart sur un panier déjà vide
        result = self.cart.clear_cart()
        
        # Vérifications
        self.assertEqual(len(self.cart.items), 0, "Cart should remain empty.")
        self.assertEqual(result, "Cart has been cleared.", "Return message should still confirm clearing.")

if __name__ == "__main__":
    unittest.main()
