numbers = []

while True:
    s = input('Enter your number or end:')
    if s == "end":
        break
    try:
        num = float(s)
        numbers.append(num)
    except ValueError:
        print("กรุณาใส่ตัวเลขหรือ end")

if len(numbers) == 0:
    print("ไม่มีข้อมูล")
else:
    print("ค่าสูงสุด:", max(numbers))
    print("ค่าต่ำสุด:", min(numbers))
