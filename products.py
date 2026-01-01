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

    def __str__(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

