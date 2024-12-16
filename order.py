


# order.py
import json

from cart import Cart
from datetime import datetime

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()
        self.status = "Pending"
        self.order_date = datetime.now()

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        self.status = "Shipped"
        return f"Order placed successfully! Total: {self.total:.2f}€, Status: {self.status}, Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
            f"\nTotal: {self.total:.2f}€\nStatus: {self.status}\nOrder Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"

              

    def generate_invoice(self):
        """Génère une facture simple avec les détails de la commande."""
        invoice = "INVOICE\n" + "-" * 20 + "\n"
        invoice += "\n".join([f"{product.name} x {quantity} = {product.price * quantity:.2f}€"
                              for product, quantity in self.items.items()])
        invoice += f"\n\nTotal: {self.total:.2f}€\n"
        invoice += "-" * 20
        return invoice

    def to_json(self):
        """Génère un récapitulatif de la commande au format JSON."""
        order_data = {
            "items": {product.name: quantity for product, quantity in self.items.items()},
            "total": self.total
        }
        return json.dumps(order_data, indent=4)

