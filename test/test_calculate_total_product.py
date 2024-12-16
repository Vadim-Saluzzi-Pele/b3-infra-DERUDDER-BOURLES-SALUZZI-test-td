import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from product import Product
from cart import Cart

class TestCartCalculateTotal(unittest.TestCase):
    def test_calculate_total_empty_cart(self):
        """Test if calculate_total returns 0 for an empty cart."""
        cart = Cart()
        self.assertEqual(cart.calculate_total(), 0, "Total for an empty cart should be 0.")

    def test_calculate_total_single_product(self):
        """Test if calculate_total works for a cart with a single product."""
        cart = Cart()
        product = Product("Laptop", 1200.0, 5)
        cart.add_product(product, 1)
        self.assertEqual(cart.calculate_total(), 1200.0, "Total for 1 Laptop should be 1200.0.")

    def test_calculate_total_multiple_products(self):
        """Test if calculate_total works for a cart with multiple products."""
        cart = Cart()
        product1 = Product("Laptop", 1200.0, 5)
        product2 = Product("Headphones", 150.0, 20)
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        expected_total = 1200.0 + (150.0 * 2)
        self.assertEqual(cart.calculate_total(), expected_total, "Total should be sum of all product prices.")

    def test_calculate_total_with_updated_quantities(self):
        """Test if calculate_total updates correctly when quantities are modified."""
        cart = Cart()
        product = Product("Laptop", 1200.0, 5)
        cart.add_product(product, 1)
        cart.add_product(product, 1)  # Adding 1 more
        self.assertEqual(cart.calculate_total(), 2400.0, "Total should reflect updated quantities.")

if __name__ == "__main__":
    unittest.main()
