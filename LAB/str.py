s = 'KritapasJirodkul'
print(s[0:8])
print(s[8:16])

word = 'banana'
if word == 'banana':
    print('Alright, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana')
if word > 'banana':
    print('Your word, ' + word + ', comes after banana')
else:
    print('Alright, banana.')

greet = 'Hello Bob'
zap = greet.lower()
print(zap)

data = 'Form staphen.marguard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 :sppos]
print(host)