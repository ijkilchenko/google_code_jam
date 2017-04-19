import sys


def read(f):
    with open(f) as file:
        lines = file.readlines()
    T = int(lines[0])
    for x, t in enumerate(range(1, T+1)):
        N = int(lines[t])
        y = solve(N)
        print('Case #%i: %s' % ((x+1), y))


def solve(N):
    N = [int(n) for n in str(N)]
    if len(N) == 1:
        return N[0]

    # len(N) > 1
    while True:
        for i, digit in enumerate(N[:-1]):
            if digit > N[i+1]:
                N[i] -= 1
                for j in range(i+1, len(N)):
                    N[j] = 9
        for i in range(len(N)-1):
            if N[i] > N[i+1]:
                break
        else:
            return int(''.join([str(n) for n in N]))


read(sys.argv[1])
