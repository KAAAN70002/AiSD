import sys
import random

sys.setrecursionlimit(200000)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    arr = [int(x) for x in input_data[1:]]
    sorted_arr = quick_sort(arr)
    print(*sorted_arr)


if __name__ == '__main__':
    main()