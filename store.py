class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def order(self, product_name: str, quantity: int) -> float:
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product.buy(quantity)

        raise Exception("Product not found")
