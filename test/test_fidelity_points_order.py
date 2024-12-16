import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from product import Product
from cart import Cart
from order import Order

class TestOrderFidelityPoints(unittest.TestCase):
    def test_fidelity_points_simple_case(self):
        """Test if fidelity points are correctly calculated for a simple order."""
        cart = Cart()
        product = Product("Laptop", 1000.0, 5)
        cart.add_product(product, 1)
        order = Order(cart)
        self.assertEqual(order.fidelity_points_order(), 100, "Fidelity points should be 10% of the total.")

    def test_fidelity_points_rounding(self):
        """Test if fidelity points are correctly rounded."""
        cart = Cart()
        product = Product("Headphones", 149.99, 10)  # Total: 149.99
        cart.add_product(product, 1)
        order = Order(cart)
        self.assertEqual(order.fidelity_points_order(), 15, "Fidelity points should round correctly.")

    def test_fidelity_points_empty_order(self):
        """Test if fidelity points are 0 for an empty cart."""
        with self.assertRaises(ValueError):
            cart = Cart()
            Order(cart)

if __name__ == "__main__":
    unittest.main()