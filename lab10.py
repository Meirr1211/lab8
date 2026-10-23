def duplicate_x(arr, x):
    result = []
    for value in arr:
        result.append(value)
        if value == x:
            result.append(value)
    return result

A = list(map(int, input("Введите массив A: ").split()))
B = list(map(int, input("Введите массив B: ").split()))
C = list(map(int, input("Введите массив C: ").split()))
XA = int(input("Число XA для массива A: "))
XB = int(input("Число XB для массива B: "))
XC = int(input("Число XC для массива C: "))

for name, arr, x in [("A", A, XA), ("B", B, XB), ("C", C, XC)]:
    result = duplicate_x(arr, x)
    print(f"{name}: размер = {len(result)}, массив = {result}")