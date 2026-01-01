import products
import store
import promotions

# setup initial stock of inventory
mac = products.Product("MacBook Air M2", price=1450, quantity=100)
bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=50)
pixel = products.Product("Google Pixel 7", price=500, quantity=250)

best_buy = store.Store([mac, bose])

# ---- TESTS ----

# Preis darf nicht negativ sein
try:
    mac.price = -100
except Exception as e:
    print("Price error OK")

# __str__ / print
print(mac)  # Erwartet: MacBook Air M2, Price: 1450, Quantity: 100

# Vergleich > <
print(mac > bose)   # True
print(bose < pixel) # True

# in-Operator
print(mac in best_buy)    # True
print(pixel in best_buy)  # False
