from products import Product


class Store:
    def __init__(self, products=None):
        if products is None:
            products = []

        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)

    # BONUS: in-Operator
    def __contains__(self, product):
        return product in self.products
