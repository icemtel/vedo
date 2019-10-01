'''
for i in range(10):
    Cone().x(i) # no variable assigned!
show(...) # show all sofar created objs
'''
from vtkplotter import Cone, collection, Text, show

for i in range(10):
    Cone(pos=[2*i, 0, 0]).color(i) # no variable assigned

Text(__doc__)

# three points, aka ellipsis, retrieves the list of all created objects
# in python 2 use collection() instead
show(..., axes=1, viewup='z')
