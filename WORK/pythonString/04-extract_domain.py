email = str(input('input your email: '))
domain = email.find('@')
sp = email.find(' ', domain)
host = email[domain+1 :sp]
print(host)