# main.py

from product import Product
from cart import Cart
from order import Order

def main():
    # Create products
    p1 = Product("Laptop", 1200.0, 5)
    p2 = Product("Headphones", 150.0, 20)
    p3 = Product("Mouse", 25.0, 50)

    # Initialize a cart
    cart = Cart()

    # Add products to the cart
    try:
        cart.add_product(p1, 1)
        cart.add_product(p2, 2)
    except ValueError as e:
        print(f"Error: {e}")

    print("Cart:")
    print(cart.display_cart())


    print("\nTesting count_unique_items function...")
    try:
        unique_items_count = cart.calculate_total_product()
        print(f"Number of unique items in the cart: {unique_items_count}")
        if unique_items_count != 2:
            raise AssertionError("count_unique_items did not return the expected result.")
        print("Test passed: count_unique_items works as expected.")
    except AssertionError as e:
        print(f"Error: {e}")

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
