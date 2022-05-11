import random

import numpy as np
from itertools import product

def main():
    n = 10  # number of lattice points
    t = 10   # number of half timesteps (#even + #odd)
    mc_steps = 5   # number of mc steps
    w_a = 0.2 # weight of a plaquettes
    w_b = 0.8 # weight of b plaquettes
    fermion = np.full((n, t), False) # fermion lattice
    bond = np.full((n//2, t), False) # bond lattice, 0 is vertical plaquette A, 1 is horizontal plaquette B
    Z = 0

    for mc in range(mc_steps):
        # calculate weights
        weight_factor = 1
        for x, y in product(range(n//2), range(t)):
            weight_factor *= w_a if not bond[x, y] else w_b
        Z += weight_factor

        # find clusters and flip
        visited = np.full((n, t), False) # record if site has been visited
        x = 0
        y = 0
        while True:
            flip = 0 if random.random() < 0.5 else 1
            while True:
                fermion[x, y] = 1 - fermion[x, y] if flip else fermion[x, y]
                visited[x, y] = True
                # upward bond
                if not bond[x//2, (y - 1)%t] and not visited[x, (y - 1)%t]:
                    y -= 1
                # downward bond
                elif not bond[x // 2, y] and not visited[x, (y + 1)%t]:
                    y += 1
                # left bond
                elif (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1) and bond[x//2, (y - 1)%t] and not visited[x - 1, y]:
                    x -= 1
                elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 0) and bond[x//2, y] and not visited[(x - 1)%n, y]:
                    x -= 1
                # right bond
                elif (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1) and bond[x//2, y] and not visited[(x + 1)%n, y]:
                    x -= 1
                elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 0) and bond[x // 2, (y - 1)%t] and not visited[(x + 1)%n, y]:
                    x -= 1
                # every existent bond visited, therefore loop closed
                else:
                    break
                x = x % n
                y = y % t
            full = False
            for i, j in product(range(n), range(t)):
                if not visited[i, j]:
                    x = i
                    y = j
                    break
                if i == n-1 and j == t-1:
                    full = True
            if full:
                break
        print(Z)




if __name__ == "__main__":
    main()