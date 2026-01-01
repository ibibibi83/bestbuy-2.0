from products import Product
from store import Store


def main():
    store = Store()

    store.add_product(Product("Laptop", 1000, 5))
    store.add_product(Product("Mouse", 50, 10))
    store.add_product(Product("Keyboard", 80, 7))

    while True:
        print("\nStore Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            store.list_products()

        elif choice == "2":
            total = store.get_total_quantity()
            print(f"Total amount in store: {total}")

        elif choice == "3":
            product_name = input("Which product do you want to buy? ")
            try:
                quantity = int(input("How many do you want? "))
                total_price = store.order(product_name, quantity)
                print(f"Total price: {total_price}")
            except Exception as e:
                print(e)

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    main()
