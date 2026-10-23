def minimum(arr):
    return min(arr)

A = list(map(int, input("Введите целые числа массива A через пробел: ").split()))
B = list(map(int, input("Введите целые числа массива B через пробел: ").split()))
C = list(map(int, input("Введите целые числа массива C через пробел: ").split()))

print("Минимум A:", minimum(A))
print("Минимум B:", minimum(B))
print("Минимум C:", minimum(C))