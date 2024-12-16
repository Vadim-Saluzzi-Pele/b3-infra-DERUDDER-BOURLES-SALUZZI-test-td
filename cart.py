from product import Product

class Cart:
    MAX_QUANTITY_PER_PRODUCT = 5  # Limitation du nombre d'exemplaires par produit

    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.MAX_QUANTITY_PER_PRODUCT:
            raise ValueError(f"Cannot add more than {self.MAX_QUANTITY_PER_PRODUCT} units of {product.name}.")
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        
        # Vérifier si le total dépasse la limite
        current_quantity = self.items.get(product, 0)
        if current_quantity + quantity > self.MAX_QUANTITY_PER_PRODUCT:
            raise ValueError(
                f"Total quantity for {product.name} exceeds the limit of {self.MAX_QUANTITY_PER_PRODUCT} units."
            )
        
        # Ajouter au panier et réduire le stock
        self.items[product] = current_quantity + quantity
        product.stock -= quantity

    def remove_product(self, product: Product):
        if product in self.items:
            # Réajuster le stock quand on retire un produit
            product.stock += self.items[product]
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def calculate_total_with_discount(self, discount_percentage: float):
        """
        Calcule le total du panier après application d'une réduction.
        :param discount_percentage: Pourcentage de réduction (0-100)
        :return: Total avec réduction
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        total = self.calculate_total()
        discount = total * (discount_percentage / 100)
        return total - discount

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])
    def calculate_total_product(self):
        if not self.items:
            return "Your cart is empty."
        return len(self.items)
    def clear_cart(self):
        self.items.clear()
        return "Cart has been cleared."

