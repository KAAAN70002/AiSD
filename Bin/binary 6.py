import sys

def main():
    n, x, y = map(int, sys.stdin.read().split())

    first = min(x, y)
    need = n - 1

    left, right = 0, need * first
    while left < right:
        mid = (left + right) // 2
        if mid // x + mid // y >= need:
            right = mid
        else:
            left = mid + 1

    print(first + left)

main()