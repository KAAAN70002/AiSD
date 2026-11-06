def main():
    c = float(input())

    left, right = 0.0, 1e5 + 1  # x^2 <= C <= 1e10, значит x <= 1e5
    for _ in range(100):
        mid = (left + right) / 2
        if mid * mid + mid ** 0.5 < c:
            left = mid
        else:
            right = mid

    print(f"{(left + right) / 2:.8f}")

main()