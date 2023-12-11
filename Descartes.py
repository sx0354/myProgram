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

a,b,*rest = range(6)
print(a,b,rest)

print("--------------------------------------------")

metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
]

print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name,cc,pop,(latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))

print('-------------------------------------------')

from collections import namedtuple

City = namedtuple('City','name country population coordinates')
Tokyo = City('Tokyo','JP',36.33,(35.68,139.69))
print(Tokyo)
print(Tokyo.population)
print(City._fields)

LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR','IN',21.935,LatLong(28.613,77.2))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())
