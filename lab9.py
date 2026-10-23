def keep_increasing(arr):
    if not arr:
        return []
    result = [arr[0]]
    for value in arr[1:]:
        if value >= result[-1]:
            result.append(value)
    return result

A = list(map(float, input("Введите массив A: ").split()))
B = list(map(float, input("Введите массив B: ").split()))
C = list(map(float, input("Введите массив C: ").split()))

for name, arr in [("A", A), ("B", B), ("C", C)]:
    result = keep_increasing(arr)
    print(f"{name}: размер = {len(result)}, массив = {result}")