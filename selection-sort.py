def selectionSort(A):
    compareCount = 0
    swapCount = 0
    for i in range(-1, -(len(A) - 1), -1):
        print(f"Elements have ben compared {compareCount} times.")
        print(f"Elements have ben swapped {swapCount} times.")
        print(f"Current array: {A}")
        maxIndex = i
        for j in range((i - 1), -(len(A) + 1), -1):
            compareCount += 1
            if A[j] > A[maxIndex]:
                swapCount += 1
                maxIndex = j
        A[i], A[maxIndex] = A[maxIndex], A[i]
    return f"Final array = [{A[0]}], [{A[1]}], [{A[2]}]...[{A[-3]}], [{A[-2]}], [{A[-1]}]"

# This brings the smallest number forward each iteration.
def selectionSortSmallToFront(A):
    compareCount = 0
    swapCount = 0
    for i in range(len(A)-1):
        print(f"Elements have ben compared {compareCount} times.")
        print(f"Elements have ben swapped {swapCount} times.")
        print(f"Current status of the array: {A}")
        minIndex = i
        for j in range(i + 1, len(A)):
            compareCount += 1
            if A[j] < A[minIndex]:
                swapCount += 1
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
    return f"A = [{A[0]}], [{A[1]}], [{A[2]}]...[{A[-3]}], [{A[-2]}], [{A[-1]}]"

# =======================
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
print(selectionSort(A1))
print(selectionSort(A2))
print(selectionSort(A3))