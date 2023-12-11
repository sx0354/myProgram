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

s = 'bicycle'
print(s[1:4:2])
print(s[::-1])
print(s[::-3])

invoice = """
... 0.....6................................40........52...55........
... 1909  Pimoroni PiBrella                    $17.50    3    $52.50
... 1489  6mm Tactile Switch x20                $4.95    2     $9.90
... 1510  Panavise Jr. - PV-201                $28.00    1    $28.00
... 1601  PiTFT Mini Kit 320x240               $34.95    1    $34.95
..."""

SKU = slice(0,6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40,52)
QUANTITY = slice(52,55)
ITEM_TOTAL = slice(55,None)

line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE],item[DESCRIPTION])

l = list(range(10))
print(l)
print(l[2:5])
l[2:5] = [20,30]

print(l)
print(l[5:8])
l[5:8] = [66,77]
print(l)

print('------------------------------')
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

row = ['_'] * 3
print(row)
print('*******')
board = []
for i in range(3): # board 包含 3个指向row的引用
    board.append(row)
print(board)
board[1][2] = '0'
print(board)

print("------")
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)

print(board)
board[1][2] = 'N'
print(board)

l = [1,2,3]
print(l,id(l))
l *= 2
print(l,id(l))

t = (1,2,3)
print(t,id(t))
t *= 2
print(t, id(t))

t = (1,2,[30,40])
#t[2] += [50,60]
print(t)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)

print(fruits.sort())
print(fruits)

print(sorted(fruits,reverse=True))
print(sorted(fruits,key=len))
print(sorted(fruits,key=len,reverse=True))
