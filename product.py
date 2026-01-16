class Product:
    """
    Represents a product that can be sold in the store.

    Returns:
        None
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a product with name, price, and quantity.

        Returns:
            None
        """
        if not name:
            raise Exception("Product name cannot be empty")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self._price = price
        self.quantity = quantity
        self.active = quantity > 0
        self._promotion = None

    # ---------- PROPERTIES ----------

    @property
    def price(self) -> float:
        """
        Returns the price of the product.

        Returns:
            float: The current price of the product.
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Sets the price of the product.

        Returns:
            None
        """
        if value < 0:
            raise Exception("Price cannot be negative")
        self._price = value

    @property
    def promotion(self):
        """
        Returns the promotion assigned to the product.

        Returns:
            Promotion or None: The assigned promotion.
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """
        Sets a promotion for the product.

        Returns:
            None
        """
        self._promotion = promotion

    # ---------- BUSINESS LOGIC ----------

    def is_active(self) -> bool:
        """
        Checks whether the product is active.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product and returns the total price.

        Returns:
            float: The total price for the purchased quantity.
        """
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise Exception("Not enough stock available")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price

    # ---------- MAGIC METHODS ----------

    def __str__(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: A formatted description of the product.
        """
        promo_text = ""
        if self.promotion:
            promo_text = f" | Promotion: {self.promotion.name}"

        return (
            f"{self.name}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
            f"{promo_text}"
        )

    def __gt__(self, other):
        """
        Compares products by price (greater than).

        Returns:
            bool: True if this product is more expensive.
        """
        return self.price > other.price

    def __lt__(self, other):
        """
        Compares products by price (less than).

        Returns:
            bool: True if this product is cheaper.
        """
        return self.price < other.price


# =====================================================


class NonStockedProduct(Product):
    """
    Represents a product that is not stock-limited.

    Returns:
        None
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a non-stocked product.

        Returns:
            None
        """
        super().__init__(name, price, quantity=0)
        self.active = True

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of a non-stocked product.

        Returns:
            float: The total price for the purchase.
        """
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def __str__(self) -> str:
        """
        Returns a string representation of the non-stocked product.

        Returns:
            str: A formatted description of the product.
        """
        promo_text = ""
        if self.promotion:
            promo_text = f" | Promotion: {self.promotion.name}"

        return f"{self.name} (Non-stocked), Price: {self.price}{promo_text}"


# =====================================================


class LimitedProduct(Product):
    """
    Represents a product with a purchase limit.

    Returns:
        None
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initializes a limited product.

        Returns:
            None
        """
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise Exception("Maximum must be greater than zero")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the limited product.

        Returns:
            float: The total price for the purchase.
        """
        if quantity > self.maximum:
            raise Exception("Cannot buy more than allowed maximum")
        return super().buy(quantity)

    def __str__(self) -> str:
        """
        Returns a string representation of the limited product.

        Returns:
            str: A formatted description of the product.
        """
        promo_text = ""
        if self.promotion:
            promo_text = f" | Promotion: {self.promotion.name}"

        return (
            f"{self.name} (Limited to {self.maximum}), "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
            f"{promo_text}"
        )
