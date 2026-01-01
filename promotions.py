from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass

class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        if quantity < 2:
            return product.price * quantity

        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items

        return (
            full_price_items * product.price
            + half_price_items * (product.price / 2)
        )

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3
        payable_items = quantity - free_items
        return payable_items * product.price
