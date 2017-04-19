import sys

def read(f):
    with open(f) as file:
        lines = file.readlines()
    T = int(lines[0])
    for x, t in enumerate(range(1, T+1)):
        S, K = lines[t].split()
        S = [s for s in S]
        y = solve(S, int(K))
        print('Case #%i: %s' % ((x+1), y))


def solve(S, K):
    num_flips = 0
    for i, _ in enumerate(S[:-K+1]):
        left_pancake = S[i]
        if left_pancake == '-':
            num_flips += 1
            flip(S, K, i)
    if sum([1 for s in S if s == '+']) == len(S):
        return num_flips
    else:
        return 'IMPOSSIBLE'


def flip(S, K, i):
    for j in range(K):
        S[i+j] = '+' if S[i+j] == '-' else '-'

read(sys.argv[1])

