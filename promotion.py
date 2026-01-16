from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for all promotion types.

    A promotion defines how a discount or special pricing
    is applied to a product during purchase.
    """

    def __init__(self, name: str):
        """
        Initializes a promotion with a name.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the promotion to a product purchase.

        Args:
            product: The product being purchased.
            quantity (int): The number of units purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage-based discount
    to the total purchase price.
    """

    def __init__(self, name: str, percent: float):
        """
        Initializes a percentage discount promotion.

        Args:
            name (str): The name of the promotion.
            percent (float): The discount percentage to apply.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies a percentage discount to the total price.

        Args:
            product: The product being purchased.
            quantity (int): The number of units purchased.

        Returns:
            float: The discounted total price.
        """
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount


class SecondHalfPrice(Promotion):
    """
    Promotion where every second item is sold at half price.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies a 'second item half price' promotion.

        Args:
            product: The product being purchased.
            quantity (int): The number of units purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        if quantity < 2:
            return product.price * quantity

        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items

        return (
            full_price_items * product.price
            + half_price_items * (product.price / 2)
        )


class ThirdOneFree(Promotion):
    """
    Promotion where every third item is free.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies a 'buy two, get one free' promotion.

        Args:
            product: The product being purchased.
            quantity (int): The number of units purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        free_items = quantity // 3
        payable_items = quantity - free_items
        return payable_items * product.price
