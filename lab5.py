def smooth_prefix_average(arr):
    result = []
    total = 0
    for k, value in enumerate(arr, start=1):
        total += value
        result.append(total / k)
    return result

A = list(map(float, input("Введите массив A: ").split()))
print("После сглаживания:", smooth_prefix_average(A))