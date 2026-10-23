def min_max_indices(arr):
    return arr.index(min(arr)) + 1, arr.index(max(arr)) + 1

A = list(map(float, input("Введите числа массива A через пробел: ").split()))
B = list(map(float, input("Введите числа массива B через пробел: ").split()))
C = list(map(float, input("Введите числа массива C через пробел: ").split()))

for name, arr in [("A", A), ("B", B), ("C", C)]:
    n_min, n_max = min_max_indices(arr)
    print(f"{name}: номер минимума = {n_min}, номер максимума = {n_max}")