import sys

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    x = list(map(int, data[2:2 + n]))

    def can(d):
        count = 1
        last = x[0]
        for i in range(1, n):
            if x[i] - last >= d:
                count += 1
                last = x[i]
                if count >= k:
                    return True
        return count >= k

    lo, hi = 1, x[-1] - x[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)

main()