def split_even_odd(arr):
    B = [value for value in arr if value % 2 == 0]
    C = [value for value in arr if value % 2 != 0]
    return B, C

A = list(map(int, input("Введите целочисленный массив A: ").split()))
B, C = split_even_odd(A)

print("B (чётные числа):", B, "размер =", len(B))
print("C (нечётные числа):", C, "размер =", len(C))