n = int(input())
a = list(map(int, input().split()))

def quicksort(a, left, right):
    if left >= right:
        return

    i, j = left, right
    pivot = a[(left + right) // 2]

    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    quicksort(a, left, j)
    quicksort(a, i, right)

quicksort(a, 0, n - 1)

print(*a)