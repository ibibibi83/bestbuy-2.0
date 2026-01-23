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
        if product.quantity < 1:
            print("The amount must be greater than 1")
            return
        if product.price <= 0:
            print("Price must be postitiv! ")
            return     
        if any(p.name == product.name for p in self.products):
            print("Product already exists ")  
            return 
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
            #print(p,product, p == product)
            if p == product:
                if p.quantity == quantity:
                    self.products.remove(product)
                    

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
    
    def get_product_by_id(self, product_id: int) -> Product:
        """
        Retrieves an active product from the store by its id.

        The search is case-insensitive and only considers active
        products returned by `get_all_products()`.

        Args:
            product_name (id): The name of the product to search for.

        Returns:
            Product: The matching Product object if found, otherwise None.
        """ 
        if product_id > len(self.products):
            return None        
        product = self.products[product_id]
        return product