import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from cart import Cart
from product import Product

class TestCartDiscount(unittest.TestCase):

    def setUp(self):
        """
        Préparation d'un environnement de test avec des produits et un panier.
        """
        self.p1 = Product("Laptop", 1200.0, 10)  # Produit 1 : Laptop
        self.p2 = Product("Headphones", 150.0, 20)  # Produit 2 : Headphones
        self.cart = Cart()
        self.cart.add_product(self.p1, 2)  # Ajoute 2 laptops
        self.cart.add_product(self.p2, 4)  # Ajoute 4 headphones

    def test_discount_valid(self):
        """
        Teste si la méthode calculate_total_with_discount applique correctement une réduction valide.
        """
        total_with_discount = self.cart.calculate_total_with_discount(10)  # 10% de réduction
        expected_total = (2 * 1200 + 4 * 150) * 0.9  # 10% de réduction appliquée
        self.assertAlmostEqual(total_with_discount, expected_total, places=2)

    def test_discount_zero(self):
        """
        Teste si une réduction de 0% retourne le total sans réduction.
        """
        total_with_discount = self.cart.calculate_total_with_discount(0)  # 0% de réduction
        expected_total = 2 * 1200 + 4 * 150  # Pas de réduction
        self.assertAlmostEqual(total_with_discount, expected_total, places=2)

    def test_discount_invalid(self):
        """
        Teste si une réduction invalide (hors de 0-100) lève une exception.
        """
        with self.assertRaises(ValueError):
            self.cart.calculate_total_with_discount(150)  # Réduction invalide (> 100)

        with self.assertRaises(ValueError):
            self.cart.calculate_total_with_discount(-10)  # Réduction invalide (< 0)

if __name__ == "__main__":
    unittest.main()
