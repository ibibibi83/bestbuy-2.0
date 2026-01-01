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
        self.promotion = None

    def is_active(self) -> bool:
        return self.active

    # Promotion setter / getter
    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise Exception("Not enough stock available")

        # Promotion berücksichtigen
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price

    def show(self) -> str:
        promo_text = ""
        if self.promotion:
            promo_text = f" | Promotion: {self.promotion.name}"

        return (
            f"{self.name}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
            f"{promo_text}"
        )

    def __str__(self) -> str:
        return self.show()


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)
        self.active = True

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def show(self) -> str:
        promo_text = ""
        if self.promotion:
            promo_text = f" | Promotion: {self.promotion.name}"

        return f"{self.name} (Non-stocked), Price: {self.price}{promo_text}"


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
        promo_text = ""
        if self.promotion:
            promo_text = f" | Promotion: {self.promotion.name}"

        return (
            f"{self.name} (Limited to {self.maximum}), "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
            f"{promo_text}"
        )
