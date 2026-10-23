def reverse_array(arr):
    arr.reverse()
    return arr

A = list(map(float, input("Введите массив A: ").split()))
B = list(map(float, input("Введите массив B: ").split()))
C = list(map(float, input("Введите массив C: ").split()))

print("A после инвертирования:", reverse_array(A))
print("B после инвертирования:", reverse_array(B))
print("C после инвертирования:", reverse_array(C))