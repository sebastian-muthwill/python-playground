"""Named tuples can be used to return values e.g. from a function
in a structured way.
This has the benefit, the data can be accessed by the attribute.
 
"""

from collections import namedtuple

Geoposition = namedtuple('Geoposition', ['latitude', 'longitude'])

position = Geoposition('49.12345', '1.12345')
print(position)
print(position.latitude)
print(position.latitude)