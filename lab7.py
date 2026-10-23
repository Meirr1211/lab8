def smooth_neighbors(arr):
    n = len(arr)
    if n <= 2:
        return arr[:]
    result = []
    for i in range(n):
        if i == 0:
            result.append((arr[i] + arr[i + 1]) / 2)
        elif i == n - 1:
            result.append((arr[i - 1] + arr[i]) / 2)
        else:
            result.append((arr[i - 1] + arr[i] + arr[i + 1]) / 3)
    return result

A = list(map(float, input("Введите массив A: ").split()))
for step in range(1, 6):
    A = smooth_neighbors(A)
    print(f"Сглаживание {step}:", A)