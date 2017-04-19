import sys

def read(f):
    with open(f) as file:
        lines = file.readlines()

    T = int(lines[0])

    for t in range(1, T+1):
        Hd, Ad, Hk, Ak, B, D = [int(s) for s in lines[t].split()]
        m = play_turn(Hd, Hd, Ad, Hk, Ak, B, D)
        print('Case #%i: %s' % (t, m))


def play_turn(H, Hd, Ad, Hk, Ak, B, D, m=0):
    if Hk < 0:
        return m
    if Hd < 0:
        return -1
    if m > 13:
        return -1

    # Attack
    m_attack = play_turn(H, Hd-Ak, Ad, Hk-Ad, Ak, B, D, m+1)
    # Buff
    m_buff = play_turn(H, Hd-Ak, Ad+B, Hk, Ak, B, D, m+1)
    # Cure
    m_cure = play_turn(H, H-Ak, Ad, Hk, Ak, B, D, m+1)
    # Debuff
    Ak_new = max(Ak - D, 0)
    m_debuff = play_turn(H, Hd-Ak_new, Ad, Hk, Ak_new, B, D, m+1)

    m = [s for s in [m_attack, m_buff, m_cure, m_debuff] if s != -1]
    if len(m) == 0:
        return -1
    else:
        return play_turn(H, Hd, Ad, Hk, Ak, B, D, min(m)+1)


read('sample.in')
#read(sys.argv[1])
