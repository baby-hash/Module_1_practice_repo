#this is a simple pizza delivery order calculator
# Purpose: Calculate the total cost of a pizza order (size + toppings + delivery).
#
# A pseudocode to guide me

# 1. ask for the user input for the size
# 2. base cost (small pizza = $8 or large pizza = $12) if
# 3. toppings $1
# 4. delivery fee (if need be)
# 5. total = base_cost + toppings + delivery_fee
# 6. print the receipt
#

# ----- Prices of pizza, delivery fee and distance for delivery -------
#
SMALL_PIZZA_PRICE = 8
LARGE_PIZZA_PRICE = 12
TOPPING_PRICE = 1
DELIVERY_FEE = 2
DELIVERY_IN_MILES = 5
EXTRA_MILE_FEE = 1

# ------ input --------
size = input("Kindly choose among `small pizza` or `large pizza`: ").strip().lower()
topping = int(input("How many toppings?: "))
radius_in_miles = int(input("How far off do you live in miles?: "))
# -- if statement of the normal COST --
#
if size == "small":
    base_cost = SMALL_PIZZA_PRICE
elif size == "large":
    base_cost  = LARGE_PIZZA_PRICE
else:
    print("Kindly choose among the two options.")
    raise SystemExit


# ------------ toppings -------------
#
toppings_cost = topping * TOPPING_PRICE


# ------------- miles --------------
#
if radius_in_miles == 0:
    delivery_fee = 0
elif radius_in_miles <= DELIVERY_IN_MILES:
    delivery_fee = DELIVERY_FEE
else:
    extra_miles = radius_in_miles - DELIVERY_IN_MILES
    delivery_fee = DELIVERY_IN_MILES + extra_miles * EXTRA_MILE_FEE


#This is the total cost
total_cost = base_cost + toppings_cost + delivery_fee


print(f"the final cost if ${total_cost}")