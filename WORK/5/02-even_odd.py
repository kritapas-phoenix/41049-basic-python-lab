number = int(input("Enter your number:"))
#รับค่าตัวแปร
ses = (number%2)
#หาเศษ
if (ses == 0):
    print("Even number")
else:
    print("Odd number")