import sys

def main():
    a, b, c, d = map(int, sys.stdin.read().split())

    if a < 0:
        a, b, c, d = -a, -b, -c, -d

    def f(x):
        return ((a * x + b) * x + c) * x + d

    left, right = -2000.0, 2000.0
    for _ in range(100):
        mid = (left + right) / 2
        if f(mid) < 0:
            left = mid
        else:
            right = mid

    print(f"{(left + right) / 2:.10f}")

main()