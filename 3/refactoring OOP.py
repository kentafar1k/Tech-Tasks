class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

class CartCalculator:
    @staticmethod
    def calculate_total(cart):
        return sum(p.price for p in cart.products)

# Использование:
cart = Cart()
cart.add_product(Product("Футболка", 25.0))
total = CartCalculator.calculate_total(cart)
print(total)  # 25.0