keb = int(input())
mid = int(input())
last = int(input())
score = keb + mid + last
print (score)
if (score >= 80):
    print("A")
elif (score >= 75 and score < 80):
    print("B+")
elif (score >= 70 and score < 75):
    print("B")
elif (score >= 65 and score < 70):
    print("C+")
elif (score >= 60 and score < 65):
    print("C")
elif (score >= 55 and score < 60):
    print("D+")
elif (score >= 50 and score < 55):
    print("D")
elif (score < 50 and score >= 0):
    print("F")