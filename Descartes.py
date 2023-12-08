import array

colors = ['black','while']
sizes = ['S','M','L']

tshirts = [(color,size) for color in colors for size in sizes]

print(tshirts)
print(len(tshirts))

symbols = '$^#@&'
mytuple = tuple(ord(symbol) for symbol in symbols)
print(mytuple)

myarray = array.array('I',(ord(symbol) for symbol in symbols))
print(myarray)

for tshirt_two in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt_two)

testnum = divmod(20,8)
print(testnum)
t = (20,8)
print(divmod(*t))
quotient,remainder = divmod(*t)
print(quotient,remainder)

import os
dirname, filenmae = os.path.split('/home/luciano/.ssh/idrsa.pub')

print(filenmae)
print(dirname)