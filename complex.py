import math , cmath
z = complex(raw_input())
print math.sqrt((z.real**2 + z.imag*2))
print cmath.phase(z)
