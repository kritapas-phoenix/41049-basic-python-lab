year = int(input("input your year:"))
#รับตัวแปร
fy = (year%4)
#หาเศษ
if (fy == 0):
        if(year%100 != 100 or year% 400 == 0):#หาร 100ได้ แล้วหาร 400ได้ไหม
              print("Leap year")
        else:
              print("Not a Leap year")
else:
    print("Not a Leap year")