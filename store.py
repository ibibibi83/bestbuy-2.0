from product import Product


class Store:
    """
    Represents a store that manages a collection of products.

    The Store class provides methods to add, remove, and query
    products, as well as to calculate quantities and manage
    product availability.
    """

    def __init__(self, products: list = None):
        """
        Initializes a new Store instance.

        If no product list is provided, an empty list is created
        to store the products.

        Args:
            products (list, optional): A list of Product objects to
                initialize the store with. Defaults to None.

        Returns:
            None
        """
        if not products:
            products = []

        self.products = products

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the store.

        This method appends a Product object to the store's
        internal product list.

        Args:
            product (Product): The product to be added to the store.

        Returns:
            None
        """
        self.products.append(product)

    def remove_product(self, product: Product, quantity: int) -> None:
        """
        Removes a specified quantity of a product from the store.

        If the requested quantity is less than the available quantity,
        the product's quantity is reduced. If the requested quantity
        equals the available quantity, the product is completely removed
        from the store. If the requested quantity exceeds the available
        quantity, an error message is printed.

        Args:
            product (Product): The product to be removed from the store.
            quantity (int): The number of units to remove.

        Returns:
            None
        """
        for p in self.products:
            if p == product:
                if p.quantity > quantity:
                    p.quantity -= quantity
                elif p.quantity == quantity:
                    self.products.remove(product)
                else:
                    print("There is to less products in store! ")

    def get_all_products(self) -> list:
        """
        Returns a list of all active products in the store.

        This method filters the store's product list and includes
        only products that are currently active. Inactive products
        are excluded from the returned list.

        Returns:
            list: A list of active Product objects available in the store.
        """
        return [product for product in self.products if product.is_active()]

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        This method iterates over all products stored in the store
        and sums up their individual quantities to determine the
        total number of items available.

        Returns:
            int: The total quantity of all products in the store.
        """
        return sum(product.quantity for product in self.products)

    # BONUS: in-Operator
    def __contains__(self, product: Product) -> bool:
        """
        Checks whether a given product exists in the store.

        This method enables the use of the `in` keyword to determine
        if a specific Product instance is present in the store's
        product list.

        Args:
            product (Product): The product to check for in the store.

        Returns:
            bool: True if the product exists in the store, False otherwise.
        """
        return product in self.products

    
    def get_product_by_name(self, product_name: str) -> Product:
        """
        Retrieves an active product from the store by its name.

        The search is case-insensitive and only considers active
        products returned by `get_all_products()`.

        Args:
            product_name (str): The name of the product to search for.

        Returns:
            Product: The matching Product object if found, otherwise None.
        """ 
        products = self.get_all_products()
        
        product = next(
            (p for p in products if p.name.lower() == product_name.lower()),
            None
        )
        return product