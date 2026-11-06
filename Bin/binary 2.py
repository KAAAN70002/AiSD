import sys

def closest(arr, x):
    # lower_bound: первый индекс, где arr[i] >= x
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    if left == 0:
        return arr[0]
    if left == len(arr):
        return arr[-1]

    # при равенстве расстояний берём меньшее число
    if x - arr[left - 1] <= arr[left] - x:
        return arr[left - 1]
    return arr[left]

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    queries = map(int, data[2 + n:2 + n + k])

    print("\n".join(str(closest(a, q)) for q in queries))

main()