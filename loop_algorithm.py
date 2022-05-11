import random

import numpy as np
from itertools import product

def main():
    n = 10  # numper of lattice points
    t = 4   # number of half timesteps (#even + #odd)
    w_a = 0.2 # weight of a plaquettes
    w_b = 0.8 # weight of b plaquettes
    fermion = np.full((n, t), False) # fermion lattice
    bond = np.full((n//2, t), False) # bond lattice, 0 is vertical plaquette A, 1 is horizontal plaquette B
    Z = 0

    # calculate weights
    weight_factor = 1
    for x, y in product(range(n//2), range(t)):
        weight_factor *= w_a if not bond[x, y] else w_b
    Z += weight_factor

    # find clusters and flip
    visited = np.full((n, t), False) # record if site has been visited
    x = 0
    y = 0
    flip = 0 if random.random() < 0.5 else 1
    while True:
        fermion[x, y] = 1 - fermion if flip else fermion
        visited[x, y] = True
        # upward bond
        if not bond[x//2, y - 1] and not visited[x, y - 1]:
            y -= 1
        # downward bond
        elif not bond[x // 2, y] and not visited[x, y + 1]:
            y += 1
        # left bond
        elif (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1) and bond[x//2, y - 1] and visited[x - 1, y]:
            x -= 1
        elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 0) and bond[x//2, y] and visited[x - 1, y]:
            x -= 1
        # right bond
        elif (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1) and bond[x//2, y] and visited[x + 1, y]:
            x -= 1
        elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 0) and bond[x // 2, y - 1] and visited[x + 1, y]:
            x -= 1
        # every existent bond occupied, therefore loop closed
        else:
            break
        x = x % n
        y = y % t




if __name__ == "__main__":
    main()