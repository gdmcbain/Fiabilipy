from pathlib import Path

from matplotlib.pyplot import subplots
from sympy import Symbol

from fiabilipy import Component, System

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

# An example of a complex system

a, b, c, d, e, f, g = [Component(f"C{i}", 1e-4) for i in range(7)]
S = System()
S["E"] = [a, b, c, g]
S[a] = S[g] = S[e] = S[d] = "S"
S[b] = S[c] = [f]
S[f] = [e, d]

print("\n# An example of a complex system")
print(f"{S.mttf=}")
print(f"{S.reliability(t)=}")

# Draw graphics

a, b = Component("a", 1e-4), Component("b", 1e-6)
S = System()
S["E"] = [a, b]
S[a] = S[b] = "S"

timerange = range(0, 20000, 100)
reliability = [S.reliability(t) for t in timerange]

fig, ax = subplots()
ax.plot(timerange, reliability)
fig.savefig(Path(__file__).with_suffix(".png"))
