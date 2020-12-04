#from Math import simple,complex   #this will not throw an error and no need to alter __init__.py file. it can be blank

from Math import * #this will throw an error because modules is not defined,
# due to which __init__.py needs to be altered from blank to
#__all__=['simple','complex']

print(simple.add(3,4))
print(complex.cube(5))