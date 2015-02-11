
from math import sin, cos
def TransfPolarCart(r,t,f):
    x= r* sin(f)* cos(t)
    y= r* sin(f)*sin(t)
    z= r* cos (f)
    
    return x,y,z
    
    
from math import asin, acos, sqrt

def TransfCartPolar(x,y,z):
    r= sqrt(x*x+y*y+z*z)
    f= acos(z/r)
    t= asin(y/(r*sin(f)))
    
    return r,t,f
