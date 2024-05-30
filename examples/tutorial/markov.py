from pathlib import Path

from matplotlib.pyplot import subplots

from fiabilipy import Component, Markovprocess

# Component and process initialization

A0, A1 = [Component(f"A{i}", 1e-4, 1.1e-3) for i in range(2)]
M0, M1 = [Component(f"M{i}", 1e-3, 1.2e-2) for i in range(2)]
components = A0, A1, M0, M1

initstates = {0: 0.9, 1: 0.1}
process = Markovprocess(components, initstates)

# Working states definition


def normal(x):
    return all(x)


def available(x):
    return (x[0] or x[1]) and (x[2] or x[3])


def damaged(x):
    return available(x) and not normal(x)


def faulty(x):
    return not available(x)


# Compute the probabilities

print(f"{process.value(150, available)=}")
print(f"{process.value(1000, normal)=}")

# Drawing plots

states = {
    "normal": normal,
    "available": available,
    "damaged": damaged,
    "faulty": faulty,
}
timerange = range(0, 6000, 10)

fig, ax = subplots()
for name, func in states.items():
    proba = [process.value(t, func) for t in timerange]
    ax.plot(timerange, proba, label=name)

ax.legend()
fig.savefig(Path(__file__).with_suffix(".png"))
