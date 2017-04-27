import sys
from collections import defaultdict

def read(f):
    with open(f) as file:
        lines = file.readlines()

    T = int(lines[0])
    line = 1
    for t in range(1, T+1):
        R, C, M, line, m = _get_case(line, lines)
        M = solve(R, C, M, m)
        print('Case #%i:' % t)
        for r in range(R):
            print(''.join(M[r]))


def _get_case(line, lines):
    R, C = [int(s) for s in lines[line].split()]
    M = []
    m = defaultdict(lambda: [])  # Letter to positions
    for r in range(R):
        row = lines[line+1+r]
        row = list(row.split()[0])
        for c in range(C):
            m[row[c]].append((r, c))
        M.append(row)
    return R, C, M, line+1+r+1, m


def solve(R, C, M, m):
    while len(m['?']) > 0: 
        for r, c in m['?']:
            for key in m.keys():
                if key != '?':
                    result = _make_largest_rectangle_with_letter(key, r, c, m, M)
                    if result == 0:
                        break  # We were able to make a larger rectangle
    return M


def _make_largest_rectangle_with_letter(letter, r, c, m, M):
    minX = -1
    maxX = -1
    minY = -1
    maxY = -1
    for x, y in m[letter] + [(r, c)]:  # For every existing position and the new position
        if minX == -1 or x < minX:
            minX = x
        if minY == -1 or y < minY:
            minY = y
        if maxX == -1 or x > maxX:
            maxX = x
        if maxY == -1 or y > maxY:
            maxY = y

    # Check if everything in the rectangle is either letter or '?'
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            if M[x][y] == letter or M[x][y] == '?':
                pass
            else:
                return 1

    # Now actually make the largest rectangle with letter
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            if M[x][y] != letter:
                M[x][y] = letter
                m[letter].append((x, y))
                m['?'].remove((x, y))
    return 0

#read('sample.in')
read(sys.argv[1])
