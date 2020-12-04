#import calc
#from calc import add,sub


#from calc import * #this practice is frowned upon because it imports all modules which might not be relevant to us

# from calc import (add,
#                  sub,
#                  CONSTANT,
#                A)
from calc import (add as addition,
                  sub as subtraction,
                  CONSTANT as C,
                  A as class_A)
#print(globals())
print(addition(3,4))
print(subtraction(9,1))
print(C)
a=class_A()
print(type(a))