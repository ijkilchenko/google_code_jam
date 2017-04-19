import sys


def read(f):
    with open(f) as file:
        lines = file.readlines()
    T = int(lines[0])
    for x, t in enumerate(range(1, T+1)):
        N, K = lines[t].split()
        y, z = solve(int(N), int(K))
        print('Case #%i: %s %s' % ((x+1), y, z))


def solve(N, K):
    L = [-1]
    L.extend([0]*N)
    L.extend([-1])

    Li = []
    Ri = []

    for k in range(K):  # For each person k
        z, y = find_pos(L, N, Li, Ri)
    return y, z


def from_left(A, L, start):
    j = start-1
    for i in range(start, len(L)-1):
        A[i] = i - j - 1
        if L[i] == -1:
            return


def from_right(A, L, start):
    j = start+1
    for i in reversed(range(1, start+1)):
        A[i] = j - i - 1
        if L[i] == -1:
            return


def find_pos(L, N, Li, Ri):
    if len(Li) == 0 and len(Ri) == 0:
        Li.extend([0] * (N + 2))
        Ri.extend([0] * (N + 2))

        from_left(Li, L, 1)
        from_right(Ri, L, len(L)-2)

    c1_list = []
    c1 = -1
    for s in range(1, len(L)-1):
        if L[s] == -1:
            continue

        c1_s = min(Li[s], Ri[s])
        if c1_s > c1 or c1 == -1:
            c1 = c1_s
            c1_list = [s]
        elif c1_s == c1:
            c1_list.append(s)

    if len(c1_list) == 1:
        assert L[c1_list[0]] != -1
        L[c1_list[0]] = -1

        from_left(Li, L, c1_list[0]+1)
        from_right(Ri, L, c1_list[0]-1)

        return min(Li[c1_list[0]], Ri[c1_list[0]]), max(Li[c1_list[0]], Ri[c1_list[0]])
    else:
        assert L[c1_list[0]] != -1
        c2_list = [c1_list[0]]
        c2 = max(Li[c1_list[0]], Ri[c1_list[0]])
        for s in c1_list[1:]:
            if L[s] == -1:
                continue

            c2_s = max(Li[s], Ri[s])
            if c2_s > c2:
                c2 = c2_s
                c2_list = [s]
            elif c2_s == c2:
                c2_list.append(s)

        assert L[c2_list[0]] != -1
        L[c2_list[0]] = -1

        from_left(Li, L, c2_list[0]+1)
        from_right(Ri, L, c2_list[0]-1)

        return min(Li[c2_list[0]], Ri[c2_list[0]]), max(Li[c2_list[0]], Ri[c2_list[0]])

#read('sample.in')
read(sys.argv[1])
