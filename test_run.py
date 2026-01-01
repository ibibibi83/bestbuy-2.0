from products import Product
from promotions import PercentDiscount

p = Product("Laptop", 1000, 5)
promo = PercentDiscount("20% OFF", 20)
p.set_promotion(promo)

print(p)
print(p.buy(2))
print(p)
