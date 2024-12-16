import json
import sys
import os

# Ajouter le chemin du dossier principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from product import Product
from cart import Cart
from order import Order

class TestOrderToJson(unittest.TestCase):
    def setUp(self):
        """Initialisation des objets pour les tests."""
        self.cart = Cart()
        self.product1 = Product("Laptop", 1200.0, 5)
        self.product2 = Product("Headphones", 150.0, 10)
        self.cart.add_product(self.product1, 2)  # Ajoute 2 laptops
        self.cart.add_product(self.product2, 3)  # Ajoute 3 écouteurs

        self.order = Order(self.cart)

    def test_to_json(self):
        """Tester la conversion de la commande en JSON."""
        result_json = self.order.to_json()

        # Charger le JSON pour vérification
        data = json.loads(result_json)
        
        # Vérifications
        expected_items = {
            "Laptop": 2,
            "Headphones": 3
        }
        self.assertEqual(data["items"], expected_items, "Les articles ne sont pas corrects dans le JSON.")
        self.assertAlmostEqual(data["total"], 1200.0 * 2 + 150.0 * 3, msg="Le total n'est pas correct dans le JSON.")

if __name__ == "__main__":
    unittest.main()
