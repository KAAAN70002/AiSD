import sys

def main():
    w, h, n = map(int, sys.stdin.read().split())

    lo, hi = 0, max(w, h) * n
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if (mid // w) * (mid // h) >= n:
            hi = mid
        else:
            lo = mid

    print(hi)

main()