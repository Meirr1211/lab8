def sort_ascending(arr):
    return sorted(arr)

A = list(map(float, input("Введите массив A: ").split()))
B = list(map(float, input("Введите массив B: ").split()))
C = list(map(float, input("Введите массив C: ").split()))

print("A:", sort_ascending(A))
print("B:", sort_ascending(B))
print("C:", sort_ascending(C))