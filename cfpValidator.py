# Exemples:
# 09828372592
# 17144842200
# ABC......JK

cpf = int(input('enter your cpf\n'))

# Extract ABC...JK from int
k=cpf%10
cpf-=k
cpf/=10
j=cpf%10
cpf-=j
cpf/=10
i=cpf%10
cpf-=i
cpf/=10
h=cpf%10
cpf-=h
cpf/=10
g=cpf%10
cpf-=g
cpf/=10
f=cpf%10
cpf-=f
cpf/=10
e=cpf%10
cpf-=e
cpf/=10
d=cpf%10
cpf-=d
cpf/=10
c=cpf%10
cpf-=c
cpf/=10
b=cpf%10
cpf-=b
cpf/=10
a=cpf%10

# Expected J
expectedJ = a*10 + b*9 + c*8 + d*7 + e*6 + f*5 + g*4 + h*3 + i*2
expectedJ = int(expectedJ % 11)
if expectedJ < 2:
    expectedJ = 0
else:
    expectedJ = 11 - expectedJ

# Expected K
expectedK = a*11 + b*10 + c*9 + d*8 + e*7 + f*6 + g*5 + h*4 + i*3 + expectedJ*2
expectedK = int(expectedK % 11)
if expectedK > 1:
    expectedK = 11 - expectedK
else:
    expectedK = 0

# Valid if (Expected X == Digit X)
if (expectedJ == j) & (expectedK == k):
    print('Valid CPF')
else:
    print('Invalid CPF')
