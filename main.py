"""
Command-line interface for managing a store.

This module provides a simple interactive menu that allows
users to list products, view total quantities, place orders,
and exit the application.
"""

from product import Product,NonStockedProduct,LimitedProduct
from store import Store


def print_products(store: Store) -> None:
    """
    Prints a list of products with their price and quantity.

    Args:
        store (Store): The Store object containing the data business logic!.

    Returns:
        None
    """
    products = store.get_all_products()
    for product in products:
        print(f"{product.name}: {product.price}$, amount: {product.quantity}")

def print_total_quantity(store: Store) -> None:
  """
  Prints the total quantity of all products in the store.

  Args:
      store (Store): The store instance whose total quantity
          should be printed.
  """
  total = store.get_total_quantity()
  print(f"Total amount in store: {total}")

def command_make_order(store: Store):
  """
  Handles the process of ordering a product from the store.

  This function prompts the user to select a product by name,
  asks for the desired quantity, processes the order, calculates
  the total price, and prints the result. If the product is not
  available or an error occurs, an appropriate message is shown.

  Args:
      store (Store): The store instance used to retrieve products
          and process the order.
  """
  product_name = input("Which product do you want to buy? ").strip()
  product = store.get_product_by_name(product_name)
  if product:
    quantity = int(input("How many do you want? "))

    try:
      store.remove_product(product, quantity)
      total_price = store.calculate_price(quantity, product.price)
      print(f"Total price: {total_price}$")
    except Exception as e:
      print(e)
  else:
    print(f"The product '{product_name}' is not available")

def main() -> None:
    """
    Runs the main store menu loop.

    This function initializes the store, adds sample products,
    and continuously prompts the user for actions until the
    user chooses to quit.

    Returns:
        None
    """
    #store = Store()

    #store.add_product(Product("Laptop", 1000, 5))
    #store.add_product(Product("Mouse", 50, 10))
    #store.add_product(Product("Keyboard", 80, 7))

    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]
    store = Store(product_list)

    while True:
        print("\nStore Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")
        print()

        if choice == "1":
            print_products(store)
        elif choice == "2":
            print_total_quantity(store)
        elif choice == "3":
            command_make_order(store)
        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    main()
