from product import Product
from cart import Cart
from order import Order

def main():
    # Créer des produits
    p1 = Product("Laptop", 1200.0, 5)
    p2 = Product("Headphones", 150.0, 20)
    p3 = Product("Mouse", 25.0, 50)

    # Initialiser un panier
    cart = Cart()

    # Ajouter des produits au panier
    try:
        cart.add_product(p1, 1)
        cart.add_product(p2, 2)
    except ValueError as e:
        print(f"Error: {e}")

    print("Cart before clearing:")
    print(cart.display_cart())

    # Option : vider le panier
    user_input = input("\nDo you want to clear the cart? (yes/no): ").strip().lower()
    if user_input == "yes":
        print("\nClearing the cart...")
        print(cart.clear_cart())

    # Afficher le contenu du panier après l'opération
    print("\nCart after clearing:")
    print(cart.display_cart())

    # Placer une commande si le panier n'est pas vide
    try:
        if cart.items:  # Vérifier que le panier n'est pas vide
            order = Order(cart)
            print("\nOrder:")
            print(order.view_order())
            print(order.place_order())
        else:
            print("\nCart is empty. Cannot place an order.")
    except ValueError as e:
        print(f"Error: {e}")

    # Vérification du stock restant
    print("\nStock after order:")
    print(p1)
    print(p2)
    print(p3)

if __name__ == "__main__":
    main()
