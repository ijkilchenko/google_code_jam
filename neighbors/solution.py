import sys
sys.setrecursionlimit(1200)


def read(f):
    with open(f) as file:
        lines = file.readlines()

    T = int(lines[0])
    line = 1
    for t in range(1, T+1):
        N, R, O, Y, G, B, V = [int(s) for s in lines[t].split()]
        y = solve(N, R, O, Y, G, B, V)
        print('Case #%i: %s' % (t, y))


def check_different(uni1, uni2):
    if uni1 == uni2:
        return False

    if uni1 == 'R':
        return False if uni2 in 'VO' else True
    elif uni1 == 'Y':
        return False if uni2 in 'OG' else True
    elif uni1 == 'B':
        return False if uni2 in 'VG' else True
    elif uni1 == 'V':
        return False if uni2 in 'RB' else True
    elif uni1 == 'O':
        return False if uni2 in 'RY' else True
    elif uni1 == 'G':
        return False if uni2 in 'YB' else True


def solve(N, R, O, Y, G, B, V, neighbors=''):
    kinds = sorted([('R', R), ('O', O), ('Y', Y), ('G', G), ('B', B), ('V', V)], key=lambda x:-x[1])

    if len(neighbors) == N:
        # We have picked all unicorns
        # Now check that first and last are different
        if check_different(neighbors[0], neighbors[-1]):
            return neighbors
        else:
            return 'IMPOSSIBLE'
    else:
        for uni in kinds:
            if 4 * uni[1] > N:
                return 'IMPOSSIBLE'

            if uni[1] > 0:
                if len(neighbors) > 0:
                    last_unicorn = neighbors[-1]
                    if check_different(last_unicorn, uni[0]):
                        pass
                    else:
                        continue

                if uni[0] == 'R':
                    new_neighbors = solve(N, R-1, O, Y, G, B, V, neighbors+'R')
                elif uni[0] == 'Y':
                    new_neighbors = solve(N, R, O, Y-1, G, B, V, neighbors+'Y')
                elif uni[0] == 'B':
                    new_neighbors = solve(N, R, O, Y, G, B-1, V, neighbors+'B')
                elif uni[0] == 'V':
                    new_neighbors = solve(N, R, O, Y, G, B, V-1, neighbors+'V')
                elif uni[0] == 'O':
                    new_neighbors = solve(N, R, O-1, Y, G, B, V, neighbors+'O')
                elif uni[0] == 'G':
                    new_neighbors = solve(N, R, O, Y, G-1, B, V, neighbors+'G')

                if new_neighbors != 'IMPOSSIBLE':
                    return new_neighbors

        return 'IMPOSSIBLE'

read('sample2.in')
#read(sys.argv[1])
