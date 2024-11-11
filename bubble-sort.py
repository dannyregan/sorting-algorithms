def bubbleSort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if (A[j] > A[j + 1]):
                A[j], A[j + 1] = A[j + 1], A[j]
    return f"Final array = [{A[0]}], [{A[1]}], [{A[2]}]...[{A[-3]}], [{A[-2]}], [{A[-1]}]"

# =======================
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
print(bubbleSort(A4))
print(bubbleSort(A5))
print(bubbleSort(A6))