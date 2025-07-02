age = int(input("input your age:"))
day = int(input("input your day:"))
#รับค่าตัวแปร
if (age < 13):
    price = 100
elif(age >= 13 and age <= 60):
    price = 180
else:
    price = 120
#หาราคา

if(day == 6 or day == 7):
    print(price + 50)
else:
    print(price)
#ดูวันหยุด และแสดงค่า