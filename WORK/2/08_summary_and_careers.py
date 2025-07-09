price = int(input("input your price:"))
tip = int(input("input your tip:"))
people = int(input("enter your amount of people"))
total = (price + (price * tip / 100)) / people
print("each person pay ", total)