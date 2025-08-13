n = int(input())

number = []

for _ in range(n):
    num = int(input())
    number.append(num)

print("มากที่สุด: ", max(number))
print("น้อยที่สด: ", min(number))