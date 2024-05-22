price = 100000
premium_customer = True
credit_score = 90

if premium_customer and credit_score > 80:
    rebate = 0.4 * price
elif premium_customer and credit_score < 80:
    rebate = 0.2 * price
else:
    rebate = 0.1 * price


print(f"Discount for the customer is $ {rebate}")    