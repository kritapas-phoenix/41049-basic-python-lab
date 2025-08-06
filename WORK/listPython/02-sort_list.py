n = int(input())
nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)
print('ลิสต์เดิม: ',nums)

nums.sort(reverse=False)

print('ลิสต์ใหม่: ',nums)