#! /usr/bin/python3.6

import collections
from pprint import pprint
import time

# named tuple collection created
Scientists = collections.namedtuple('Scientists', 
                                   ['name', 'born', 'field', 'nobel'])

# immutable data structure of tuple of namedtuples
scientists = (
    Scientists(name='Ada', born=1895, field='physics', nobel=True),
    Scientists(name='John', born=1991, field='chemistry', nobel=True),
    Scientists(name='Brown', born=1998, field='computer science', nobel=True),
    Scientists(name='Luck', born=1850, field='physics', nobel=False),
    Scientists(name='Real', born=1948, field='chemistry', nobel=False),
    Scientists(name='Path', born=1962, field='economics', nobel=True),
    Scientists(name='King', born=1961, field='computer science', nobel=True),
)
pprint(scientists)
print()

# function to be passed to map, transforming the data
def transform(entry):
    print(f'Processing entry {entry.name}...')
    time.sleep(1)
    return {'name':entry.name, 'age':2018-entry.born}
    print(f'Done processing entry {entry.name}...')

# map to create new tuple of defaultdicts
now = time.time()
name_and_age = tuple(map(transform, scientists))
end = time.time()
print()

print(f'Time to transform data : {end - now:.2f}s')
print()

pprint(name_and_age)