import sys

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))

    lo, hi = 0, max(a) + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if sum(x // mid for x in a) >= k:
            lo = mid
        else:
            hi = mid

    print(lo)

main()