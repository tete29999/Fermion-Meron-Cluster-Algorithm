import random

import numpy as np
from itertools import product

def main():
    n = 12  # number of lattice points
    t = 12   # number of half timesteps (#even + #odd)
    b = 1 # beta
    mc_steps = 50000   # number of mc steps
    w_a = np.cosh(b/t)  # weight of a plaquettes U = t = 1
    w_b = np.sinh(b/t)  # weight of b plaquettes
    fermion = np.full((n, t), False)    # fermion lattice
    bond = np.full((n//2, t), False)    # bond lattice, 0 is vertical plaquette A, 1 is horizontal plaquette B
    Z = 0

    for mc in range(mc_steps):
        # find clusters and flip
        visited = np.full((n, t), False)    # record if site has been visited
        x = 0
        y = 0
        while True:
            flip = 0 if random.random() < 0.5 else 1
            while True:
                fermion[x, y] = 1 - fermion[x, y] if flip else fermion[x, y]
                visited[x, y] = True
                if x % 2 == 0 and y % 2 == 0:
                    # top
                    if not bond[(x//2 - 1)%(t//2), y - 1] and not visited[x, (y-1)%t]:
                        y -= 1
                    # left
                    elif bond[(x//2 - 1)%(t//2), y - 1] and not visited[(x-1)%t, y]:
                        x -= 1
                    # bottom
                    elif not bond[x//2, y] and not visited[x, (y+1)%t]:
                        y += 1
                    # right
                    elif bond[x//2, y] and not visited[(x+1)%t, y]:
                        x += 1
                    # closed loop
                    else:
                        break
                elif x % 2 == 1 and y % 2 == 0:
                    # top
                    if not bond[x//2, y - 1] and not visited[x, (y-1)%t]:
                        y -= 1
                    # left
                    elif bond[x//2, y] and not visited[(x-1)%t, y]:
                        x -= 1
                    # bottom
                    elif not bond[x//2, y] and not visited[x, (y+1)%t]:
                        y += 1
                    # right
                    elif bond[x//2, y-1] and not visited[(x+1)%t, y]:
                        x += 1
                    # closed loop
                    else:
                        break
                elif x % 2 == 0 and y % 2 == 1:
                    # top
                    if not bond[x//2, y - 1] and not visited[x, (y-1)%t]:
                        y -= 1
                    # left
                    elif bond[(x//2 - 1)%(t//2), y] and not visited[(x-1)%t, y]:
                        x -= 1
                    # bottom
                    elif not bond[(x//2 - 1)%(t//2), y] and not visited[x, (y+1)%t]:
                        y += 1
                    # right
                    elif bond[x//2, y-1] and not visited[(x+1)%t, y]:
                        x += 1
                    # closed loop
                    else:
                        break
                elif x % 2 == 1 and y % 2 == 1:
                    # top
                    if not bond[x//2, y - 1] and not visited[x, (y-1)%t]:
                        y -= 1
                    # left
                    elif bond[x//2, y - 1] and not visited[(x-1)%t, y]:
                        x -= 1
                    # bottom
                    elif not bond[x//2, y] and not visited[x, (y+1)%t]:
                        y += 1
                    # right
                    elif bond[x//2, y] and not visited[(x+1)%t, y]:
                        x += 1
                    # closed loop
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

        # cluster assignment
        for x, y in product(range(0, n, 2), range(t)):
            if fermion[x, y] == fermion[x, (y + 1) % t] == fermion[(x + 1) % n, y] == fermion[(x + 1) % n, (y + 1) % t]:
                bond[x // 2, y] = False
            if fermion[x, y] != fermion[x, (y + 1) % t]:
                bond[x// 2, y] = True
            else:
                bond[x // 2, y] = False if random.random() < w_a/(w_a + w_b) else True

        # calculate weights
        weight_factor = 1
        for x, y in product(range(n // 2), range(t)):
            weight_factor *= w_a if not bond[x, y] else w_b
        Z += weight_factor
        #print(weight_factor)

    print(Z)

if __name__ == "__main__":
    main()