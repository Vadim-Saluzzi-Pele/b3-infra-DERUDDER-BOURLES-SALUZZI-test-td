import sys
import os

# Ajouter le chemin du dossier principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from product import Product
from cart import Cart
from order import Order

class TestOrderGenerateInvoice(unittest.TestCase):
    def setUp(self):
        """Initialisation des objets pour les tests."""
        self.cart = Cart()
        self.product1 = Product("Laptop", 1200.0, 5)
        self.product2 = Product("Headphones", 150.0, 10)
        self.cart.add_product(self.product1, 2)  # Ajoute 2 laptops
        self.cart.add_product(self.product2, 3)  # Ajoute 3 écouteurs

        self.order = Order(self.cart)

    def test_generate_invoice(self):
        """Tester la génération de la facture."""
        invoice = self.order.generate_invoice()

        # Vérifications sur le format de la facture
        self.assertIn("INVOICE", invoice, "La facture doit contenir le titre INVOICE.")
        self.assertIn("Laptop x 2", invoice, "La facture doit inclure le produit Laptop avec la bonne quantité.")
        self.assertIn("Headphones x 3", invoice, "La facture doit inclure le produit Headphones avec la bonne quantité.")
        self.assertIn("Total: 2850.00€", invoice, "Le total doit être correctement affiché dans la facture.")


if __name__ == "__main__":
    unittest.main()
