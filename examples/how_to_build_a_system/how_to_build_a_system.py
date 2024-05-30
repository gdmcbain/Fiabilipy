from fiabilipy import Component
from sympy import Symbol

t = Symbol("t", positive=True)
comp = Component("C0", 1e-4)

print(f"{comp.mttf=}")
print(f"{comp.reliability(1000)=}")
print(f"{comp.reliability(t)=}")
print(f"{comp.reliability(t=100)=}")
