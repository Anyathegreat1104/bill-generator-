bill = int(input("Enter your restaurant bill: "))
membership = input("Do you have a membership card? (yes/no): ")
if membership == "yes":
    discount = bill * 10 / 100
else:
    discount = 0
finalBill = bill - discount
print("Your bill is:", bill)
print("Discount is:", discount)
print("Final bill is:", finalBill)