n = int(input())

even_list = []
odd_list = []

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("เลขคู่: ", even_list)
print("เลขคี่: ", odd_list)