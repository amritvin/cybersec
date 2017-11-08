mystring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
from itertools import product
combos = [''.join(i) for i in product(mystring, repeat = 8)]
print combos
