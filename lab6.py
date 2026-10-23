def smooth_once(arr):
    if len(arr) < 2:
        return arr[:]
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append((arr[i - 1] + arr[i]) / 2)
    return result

A = list(map(float, input("Введите массив A: ").split()))
for step in range(1, 6):
    A = smooth_once(A)
    print(f"Сглаживание {step}:", A)