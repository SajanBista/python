# This file is used to call two modules of the package "math_package"
# Import Modules from a Package
# Syntax is : import <package_name>.<module_name>
##import math_package
##import math_package.addition
#%%

# We can also use this syntax to import modules
# Syntax: from <package name> import <module name>
from math_package import addition
from math_package import subtraction
from math_package import mul_pow

res_add = addition.add(3, 7)
res_sub = subtraction.sub(9, 4)
res_mul = mul_pow.mul(5, 9)
res_pow = mul_pow.power(5, 2)
print(res_add)
print(res_sub)
print(res_mul)
print(res_pow)
#%%