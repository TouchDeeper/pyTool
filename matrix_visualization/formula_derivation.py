from sympy import *


J11, J12, J21, J22, J31, J32, r1, r2, r3 = symbols("J11, J12, J21, J22, J31, J32, r1, r2, r3")
a, b, c, d, e, f = symbols("a, b, c, d, e, f")
J = Matrix([[J11, J12],
            [J21, J22],
            [J31, J32]])
I = Matrix([[a, d, e],
            [d, b, f],
            [e, f, c]])
JTJ = J.T * I * J
r = Matrix([r1,
            r2,
            r3])
delta_x = -JTJ.inv() * J.T * I * r
pprint(simplify(delta_x))
