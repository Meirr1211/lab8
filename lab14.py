def split_by_position(arr):
    B = arr[0::2]  # позиции 1, 3, 5... в обычной нумерации
    C = arr[1::2]  # позиции 2, 4, 6...
    return B, C

A = list(map(float, input("Введите массив A: ").split()))
B, C = split_by_position(A)

print("B (нечётные порядковые номера):", B, "размер =", len(B))
print("C (чётные порядковые номера):", C, "размер =", len(C))