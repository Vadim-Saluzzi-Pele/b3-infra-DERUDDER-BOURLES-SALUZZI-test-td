
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
