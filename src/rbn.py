import itertools
import random

import numpy as np
from PIL import Image

k = 50 # connections
l = 1000


def get_truth_table():
    inputs = [
        (1, 1, 1),
        (1, 1, 0),
        (1, 0, 1),
        (1, 0, 0),
        (0, 1, 1),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 0),
    ]
    outputs = random.choices([0, 1], k=8)
    return dict(zip(inputs, outputs))


def apply_rule(state, truth_table):
    neighbors = [
        (state[connections[i][0]], state[connections[i][1]], state[connections[i][2]])
        for i in range(len(state))
    ]
    return [truth_table[e] for e in neighbors]


for j in range(500):
    ttable = get_truth_table()
    initial_state = random.choices([0, 1], k=k)
    connections = random.choices(list(itertools.combinations(list(range(k)), 3)), k=k)
    booleans = [initial_state]

    for i in range(l - 1):
        state = booleans[-1]
        new_state = apply_rule(state, ttable)
        booleans.append(new_state)
        if i % random.randint(2, 30) == 0:
            ttable = get_truth_table()
    booleans = np.asarray(booleans).transpose().astype("uint8") * 255
    img = Image.fromarray(booleans)
    img = img.resize((3000, 1500))
    fname = f"outputs/{str(j).zfill(4)}.png"
    print(fname)
    img.save(fname)
