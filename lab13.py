def bell_order(arr):
    values = sorted(arr)
    result = []
    left, right = 0, len(values) - 1
    while left <= right:
        result.append(values[left])
        left += 1
        if left <= right:
            result.append(values[right])
            right -= 1
    return result

A = list(map(float, input("Введите массив A: ").split()))
B = list(map(float, input("Введите массив B: ").split()))
C = list(map(float, input("Введите массив C: ").split()))

print("A:", bell_order(A))
print("B:", bell_order(B))
print("C:", bell_order(C))