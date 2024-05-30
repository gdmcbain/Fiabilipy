import pylab as p
from fiabilipy import Component, System

motor = Component("M", 1e-4, 3e-2)
powers = [Component("P{}".format(i), 1e-6, 2e-4) for i in (0, 1)]
S = System()
S["E"] = [powers[0], powers[1]]
S[powers[0]] = S[powers[1]] = [motor]
S[motor] = "S"
S.draw()
p.show()
