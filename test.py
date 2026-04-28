import sys

def solve():
    filename = '26_2580.txt'
    try:
        with open(filename, 'r') as f:
            data = f.read().split()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        sys.exit(1)

    if not data:
        print(0, 0)
        return

    it = iter(data)
    try:
        N = int(next(it))
        K = int(next(it))
    except StopIteration:
        print("Ошибка формата входных данных.")
        return

    DAY_MS = 24 * 3600 * 1000
    WIN_START = K
    WIN_END = K + DAY_MS

    events = []
    for _ in range(N):
        s = int(next(it))
        e = int(next(it))

        start = s if s != 0 else WIN_START
        end = e if e != 0 else WIN_END

        start = max(start, WIN_START)
        end = min(end, WIN_END)

        if start < end:
            events.append((start, 1))
            events.append((end, -1))

    events.sort()

    max_cnt = 0
    cur_cnt = 0
    max_dur = 0
    last_t = events[0][0]

    for t, typ in events:
        dt = t - last_t
        if dt > 0:
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt
                max_dur = dt
            elif cur_cnt == max_cnt:
                max_dur += dt
        cur_cnt += typ
        last_t = t

    print(max_cnt, max_dur)

if __name__ == '__main__':
    solve()