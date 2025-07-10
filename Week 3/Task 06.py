#  Task 6:
# Billing system:
# Take number of products and total price.
# If price > 1000 and products > 3 → 15% discount
# If price > 500 → 10% discount
# Else → No discount.
# Show final bill.

products = int(input("Enter the number of products : "))
total_price = int(input("Enter the total price : "))

if total_price > 1000 and products > 3 :
    discount = 0.15
    print("10% discount")
    
elif total_price > 500:
    discount = 0.10
    print("10% discount")
    
else:
    discount = 0
    print("No discount")
final_price = total_price - (total_price * discount)
print(f"Final bill is : {final_price}")