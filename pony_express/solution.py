import sys


def read(f):
    with open(f) as file:
        lines = file.readlines()

    T = int(lines[0])
    line = 1
    for t in range(1, T+1):
        N, Q, H, A, UV, line = _get_case(line, lines)
        y = solve(N, Q, H, A, UV)
        print('Case #%i: %0.6f' % (t, y))


def _get_case(line, lines):
    N, Q = [int(s) for s in lines[line].split()]
    H = []
    for r in range(N):
        row = [int(s) for s in lines[line+1+r].split()]
        H.append(row)
    line = line + 1 + r
    A = []
    for r in range(N):
        row = [int(s) for s in lines[line+1+r].split()]
        A.append(row)
    line = line + 1 + r
    UV = []
    for r in range(Q):
        row = [int(s) for s in lines[line+1+r].split()]
        UV.append(row)
    line = line + 1 + r
    return N, Q, H, A, UV, line


def solve(N, Q, H, A, UV):
    city = 0
    horse = H[0]

    visited = []
    queue = [0]

read('sample.in')
#read(sys.argv[1])
