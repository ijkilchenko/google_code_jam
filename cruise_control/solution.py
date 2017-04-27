import sys


def read(f):
    with open(f) as file:
        lines = file.readlines()

    T = int(lines[0])
    line = 1
    for t in range(1, T+1):
        D, N, H, line = _get_case(line, lines)
        y = solve(D, N, H)
        print('Case #%i: %0.6f' % (t, y))


def _get_case(line, lines):
    D, N = [int(s) for s in lines[line].split()]
    H = []
    for h in range(N):
        row = [int(s) for s in lines[line+1+h].split()]
        H.append(row)
    line = line+2+h
    return D, N, H, line


def solve(D, N, H):
    H = sorted(H, key=lambda x: x[0])

    t_last_horse_finish = (D - H[-1][0])/H[-1][1]

    for i in range(2, len(H)+1):
        t_a = t_last_horse_finish
        t_b = (D - H[-i][0])/H[-i][1]

        if t_a > t_b:
            t_last_horse_finish = t_a
        else:
            t_last_horse_finish = t_b

    v_Annie = D/t_last_horse_finish

    return v_Annie

#read('sample2.in')
read(sys.argv[1])
