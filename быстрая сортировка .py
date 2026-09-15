import random
import sys

sys.setrecursionlimit(200000)


def quicksort(arr, low, high):
    while low < high:
        pivot = arr[random.randint(low, high)]
        lt = low
        gt = high
        i = low

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
            else:
                i += 1

        if lt - low < high - gt:
            quicksort(arr, low, lt - 1)
            low = gt + 1
        else:
            quicksort(arr, gt + 1, high)
            high = lt - 1


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1 : n + 1]]

    if arr:
        quicksort(arr, 0, len(arr) - 1)

    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    main()