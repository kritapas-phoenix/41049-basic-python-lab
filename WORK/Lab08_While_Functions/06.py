def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

print('calculator')
print('enter 1 to plus')
print('enter 2 to minus')
print('enter 3 to multiply')
print('enter 4 to stop')

f = 0
while f != 4:
    f = int(input('input your mode:'))
    if f == 4:
        print("Goodbye!")
        break
    nf = int(input('enter your first number:'))
    ns = int(input('enter your second number:'))
    if f == 1:
        print("Result:", plus(nf, ns))
    elif f == 2:
        print("Result:", minus(nf, ns))
    elif f == 3:
        print("Result:", multiply(nf, ns))
    else:
        print("Invalid mode, try again.")
