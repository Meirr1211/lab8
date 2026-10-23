def index_array(arr):
    # Номера элементов в порядке возрастания значений, начиная с 1
    return [i + 1 for i in sorted(range(len(arr)), key=lambda i: arr[i])]

A = list(map(float, input("Введите массив A: ").split()))
B = list(map(float, input("Введите массив B: ").split()))
C = list(map(float, input("Введите массив C: ").split()))

for name, arr in [("A", A), ("B", B), ("C", C)]:
    print(f"{name} исходный:", arr)
    print(f"Индексный массив {name}:", index_array(arr))