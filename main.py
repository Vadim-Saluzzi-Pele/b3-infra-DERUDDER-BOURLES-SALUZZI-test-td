from product import Product
from cart import Cart
from order import Order

def main():
    # Create products
    p1 = Product("Laptop", 1200.0, 20)
    p2 = Product("Headphones", 150.0, 20)
    p3 = Product("Mouse", 25.0, 50)

    # Initialize a cart
    cart = Cart()

    # Add products to the cart
    try:
        cart.add_product(p1, 3)
        cart.add_product(p2, 4)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nCart:")
    print(cart.display_cart())

    # Demander une réduction à l'utilisateur
    discount_percentage = 0
    try:
        discount_percentage = float(input("\nEnter a discount percentage (0-100): "))
        total_with_discount = cart.calculate_total_with_discount(discount_percentage)
        print(f"\nTotal after applying {discount_percentage}% discount: {total_with_discount:.2f}€")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Place an order
    try:
        order = Order(cart)
        print("\nOrder:")
        print(order.view_order())
        print(order.place_order())
    except ValueError as e:
        print(f"Error: {e}")

    # Check remaining stock
    print("\nStock after order:")
    print(p1)
    print(p2)
    print(p3)

if __name__ == "__main__":
    main()


