import random

import numpy as np
from itertools import product

def main():
    n = 10  # numper of lattice points
    t = 4   # number of half timesteps (#even + #odd)
    w_a = 0.2 # weight of a plaquettes
    w_b = 0.8 # weight of b plaquettes
    fermions = np.full((n, t), False) # fermion lattice
    bonds = np.full((n//2, t), False) # bond lattice, 0 is plaquette A, 1 plaquette B
    Z = 0

    # calculate weights
    weight_factor = 1
    for x, y in product(range(n//2), range(t)):
        weight_factor *= w_a if not bonds[x, y] else w_b
    Z += weight_factor

    # find clusters and flip
    visited = np.full((n, t), False) # record if site has been visited
    x = 0
    y = 0
    flip = 0 if random.random() < 0.5 else 1






if __name__ == "__main__":
    main()