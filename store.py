class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for index, product in enumerate(self.products, start=1):
            print(f"{index}. {product}")

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            if product.is_active():
                total += product.quantity
        return total
