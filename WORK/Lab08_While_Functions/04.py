n = int(input('Enter your number: '))
o = n
factorial = 1

while n > 1 :
    factorial *= n
    n = n-1
print (o,'! =', factorial)