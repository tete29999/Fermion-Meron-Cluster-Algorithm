import random
import numpy as np
from itertools import product

def mc_step(n, t, w_a, w_b, sign):
    # find clusters and flip
    visited = np.full((n, t), False)  # record if site has been visited
    x = 0
    y = 0
    new_sign = sign

    while True:
        flip = 0 if random.random() < 0.5 else 1  # decide if next cluster is to be flipped
        while True:
            visited_this_loop = np.full((n, t), False)
            n_h = 0 # number of horizontal plaquettes empty -> occupied for sign
            n_w = 0 # number of time loops
            fermion[x, y] = 1 - fermion[x, y] if flip else fermion[x, y]  # flip
            visited[x, y] = True
            visited_this_loop[x, y] = True
            # follow bond loop
            if x % 2 == 0 and y % 2 == 0:
                # top
                if not bond[(x // 2 - 1) % (n // 2), (y - 1) % t] and not visited[x, (y - 1) % t]:
                    if y == 0:
                        n_w += 1
                    y -= 1
                # left
                elif bond[(x // 2 - 1) % (n // 2), (y - 1) % t] and not visited[(x - 1) % n, y]:
                    if fermion[(x-1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x -= 1
                # bottom
                elif not bond[x // 2, y] and not visited[x, (y + 1) % t]:
                    if y == t - 1:
                        n_w += 1
                    y += 1
                # right
                elif bond[x // 2, y] and not visited[(x + 1) % n, y]:
                    if fermion[(x + 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x += 1
                # closed loop
                else:
                    # up
                    if y == 0 and not bond[(x // 2 - 1) % (n // 2), (y - 1) % t] and visited_this_loop[x, (y - 1) % t]:
                        n_w += 1
                    # down
                    elif y == t - 1 and not bond[x // 2, y] and visited_this_loop[x, (y + 1) % t]:
                        n_w += 1
                    # left
                    elif bond[(x // 2 - 1) % (n // 2), (y - 1) % t] and visited_this_loop[(x - 1) % n, y]:
                        if fermion[(x - 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                    # right
                    elif bond[x // 2, y] and visited_this_loop[(x + 1) % n, y]:
                        if fermion[(x + 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                        x += 1
                    break
            elif x % 2 == 1 and y % 2 == 0:
                # top
                if not bond[x // 2, (y - 1) % t] and not visited[x, (y - 1) % t]:
                    if y == 0:
                        n_w += 1
                    y -= 1
                # left
                elif bond[x // 2, y] and not visited[(x - 1) % n, y]:
                    if fermion[(x - 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x -= 1
                # bottom
                elif not bond[x // 2, y] and not visited[x, (y + 1) % t]:
                    if y == t - 1:
                        n_w += 1
                    y += 1
                # right
                elif bond[x // 2, (y - 1) % t] and not visited[(x + 1) % n, y]:
                    if fermion[(x + 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x += 1
                # closed loop
                else:
                    # up
                    if y == 0 and not bond[x // 2, (y - 1) % t] and visited_this_loop[x, (y - 1) % t]:
                        n_w += 1
                    # down
                    elif y == t - 1 and not bond[x // 2, y] and visited_this_loop[x, (y + 1) % t]:
                        n_w += 1
                    # left
                    elif bond[x // 2, y] and visited_this_loop[(x - 1) % n, y]:
                        if fermion[(x - 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                    # right
                    elif bond[x // 2, (y - 1) % t] and visited_this_loop[(x + 1) % n, y]:
                        if fermion[(x + 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                        x += 1
                    break
            elif x % 2 == 0 and y % 2 == 1:
                # top
                if not bond[x // 2, (y - 1) % t] and not visited[x, (y - 1) % t]:
                    if y == 0:
                        n_w += 1
                    y -= 1
                # left
                elif bond[(x // 2 - 1) % (n // 2), y] and not visited[(x - 1) % n, y]:
                    if fermion[(x - 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x -= 1
                # bottom
                elif not bond[(x // 2 - 1) % (n // 2), y] and not visited[x, (y + 1) % t]:
                    if y == t - 1:
                        n_w += 1
                    y += 1
                # right
                elif bond[x // 2, (y - 1) % t] and not visited[(x + 1) % n, y]:
                    if fermion[(x + 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x += 1
                # closed loop
                else:
                    # up
                    if y == 0 and not bond[x // 2, (y - 1) % t] and visited_this_loop[x, (y - 1) % t]:
                        n_w += 1
                    # down
                    elif y == t - 1 and not bond[(x // 2 - 1) % (n // 2), y] and visited_this_loop[x, (y + 1) % t]:
                        n_w += 1
                    # left
                    elif bond[(x // 2 - 1) % (n // 2), y] and visited_this_loop[(x - 1) % n, y]:
                        if fermion[(x - 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                    # right
                    elif bond[x // 2, (y - 1) % t] and visited_this_loop[(x + 1) % n, y]:
                        if fermion[(x + 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                        x += 1
                    break
            elif x % 2 == 1 and y % 2 == 1:
                # top
                if not bond[x // 2, (y - 1) % t] and not visited[x, (y - 1) % t]:
                    if y == 0:
                        n_w += 1
                    y -= 1
                # left
                elif bond[x // 2, (y - 1) % t] and not visited[(x - 1) % n, y]:
                    if fermion[(x - 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x -= 1
                # bottom
                elif not bond[x // 2, y] and not visited[x, (y + 1) % t]:
                    if y == t - 1:
                        n_w += 1
                    y += 1
                # right
                elif bond[x // 2, y] and not visited[(x + 1) % n, y]:
                    if fermion[(x + 1) % n, y]:
                        if fermion[x, y]:
                            n_h += 1
                    x += 1
                # closed loop
                else:
                    # up
                    if y == 0 and not bond[x // 2, (y - 1) % t] and visited_this_loop[x, (y - 1) % t]:
                        n_w += 1
                    # down
                    elif y == t - 1 and not bond[x // 2, y] and visited_this_loop[x, (y + 1) % t]:
                        n_w += 1
                    # left
                    elif bond[x // 2, (y - 1) % t] and visited_this_loop[(x - 1) % n, y]:
                        if fermion[(x - 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                    # right
                    elif bond[x // 2, y] and visited_this_loop[(x + 1) % n, y]:
                        if fermion[(x + 1) % n, y]:
                            if fermion[x, y]:
                                n_h += 1
                        x += 1
                    break
            x = x % n  # boundary conditions
            y = y % t
            if flip:
                new_sign *= (-1)**(n_w + n_h + 1)

        full = False
        for i, j in product(range(n), range(t)):
            if not visited[i, j]:
                x = i
                y = j
                break
            if i == n - 1 and j == t - 1:
                full = True  # if last indices are reached everything has been visited
        if full:
            break

    # bond assignment
    for x, y in product(range(n), range(t)):
        if y % 2 != x % 2:
            continue
        # all occupied or all unoccupied
        if fermion[x, y] == fermion[(x + 1) % n, y] and fermion[x, (y + 1) % t] == fermion[(x + 1) % n, (y + 1) % t]:
            bond[x // 2, y] = False
        # diagonal occupation
        elif fermion[x, y] != fermion[x, (y + 1) % t]:
            bond[x // 2, y] = True
        # parallel occupation
        else:
            bond[x // 2, y] = False if random.random() < w_a / (w_a + w_b) else True
        # calculate bond config in nicer lattice for debugging purposes
        bond_debug[x, y] = bond[x // 2, y]

    return new_sign


def main():
    global fermion
    global bond
    global bond_debug
    n = 4  # number of lattice points
    t = 10   # number of half timesteps (#even + #odd)
    b = 0.001 # beta
    mc_steps = 500000   # number of mc steps
    initial_mc_steps = 5000
    w_a = np.cosh(b/t)  # weight of a plaquettes U = t = 1
    w_b = np.sinh(b/t)  # weight of b plaquettes

    fermion = np.full((n, t), False)    # fermion lattice initialized to empty
    # bond lattice is squashed down and initalized to vertical plaquettes
    bond = np.full((n//2, t), False)    # bond lattice, 0 is vertical plaquette A, 1 is horizontal plaquette B

    Z_0 = 0
    n_avg = 0
    avg_sign = 0

    #random.seed(42)
    bond_debug = np.full((n, t), - 1) # only for debugging purposes
    sign = 1 # guess?

    for mc in range(initial_mc_steps):
        sign = mc_step(n, t, w_a, w_b, sign)

    for mc in range(mc_steps):

        sign = mc_step(n, t, w_a, w_b, sign)

        # calculate weight of configuration
        weight_factor = 1
        for x, y in product(range(n // 2), range(t)):
            weight_factor *= w_a if not bond[x, y] else w_b
        Z_0 += weight_factor

        # calculate average sign
        avg_sign += sign * weight_factor

        # calculate average occupancy
        n_occupied = 0
        for x in range(n):
            if fermion[x, 0]:
                n_occupied += 1
            else:
                n_occupied -= 1
        n_avg += n_occupied / n * sign * weight_factor

        if mc % 10000 == 0:
            print(f'Z_0 = {Z_0}',)
            print(f'avg_sign = {avg_sign / Z_0 }')
            print(f'n_avg = {n_avg / avg_sign}')
            print('________________________________')

    print(f'Z_0 = {Z_0}', )
    print(f'avg_sign = {avg_sign /Z_0}')
    print(f'n_avg = {n_avg / avg_sign}')

if __name__ == "__main__":
    main()