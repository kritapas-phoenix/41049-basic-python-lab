price = float(input("Enter your price:"))
#รับค่า
if price >= 2000:
    fp = price * 85 / 100
elif price >= 1000:
    fp = price * 90 / 100
elif price >= 500:
    fp = price * 95 / 100
else:
    fp = price
#ดูส่วนลด
print(fp)
#แสดงคำตอบ