from fiabilipy import Component, System
from sympy import Symbol

# Building components

t = Symbol("t", positive=True)
comp = Component("C0", 1e-4)

print("\n# Building components")
print(f"{comp.mttf=}")
print(f"{comp.reliability(1000)=}")
print(f"{comp.reliability(t)=}")
print(f"{comp.reliability(t=100)=}")

# Gather components to build a system

power = Component("P0", 1e-6)
motor = Component("M0", 1e-3)
S = System()
S["E"] = [power]
S[power] = [motor]
S[motor] = "S"

print("\n# Gather components to build a system")
print(f"{S.mttf=}")
print(f"{float(S.mttf)=}")
print(f"{S.reliability(t)=}")