#! /usr/bin/python3.6

import collections
from pprint import pprint

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

# reduce function
def transform(entry):
    return {'name':entry.name, 'age':2018-entry.born}

# map to create new tuple of defaultdicts
name_and_age = tuple(map(transform, scientists))
print()
pprint(name_and_age)