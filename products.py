class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise Exception("Product name cannot be empty")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self) -> bool:
        return self.active

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise Exception("Not enough stock available")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def __str__(self) -> str:
        return self.show()


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)
        self.active = True

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")
        return self.price * quantity

    def show(self) -> str:
        return f"{self.name} (Non-stocked), Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise Exception("Maximum must be greater than zero")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise Exception("Cannot buy more than allowed maximum")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name} (Limited to {self.maximum}), Price: {self.price}, Quantity: {self.quantity}"
