# Compares neighboring elements and swaps them if their not in ascending order. When the array is sorted, the program returns the array.
def bubbleSort(A):
    prevSwapCount = 0
    swapCount = 1
    compareCount = 0
    for i in range(len(A) - 1):
        print(f"Elements have ben compared {compareCount} times.")
        print(f"Elements have ben swapped {swapCount - 1} times.")
        print(f"Current array: {A}")
        # If the following returns false, the array is sorted.
        if prevSwapCount != swapCount:
            prevSwapCount = swapCount
            # Compare neighboring elements.
            for j in range(len(A) - i - 1):
                compareCount += 1
                # If they're not in ascending order, swap them.
                if (A[j] > A[j + 1]):
                    swapCount += 1
                    A[j], A[j + 1] = A[j + 1], A[j]
        else:
            return f"Final array = [{A[0]}], [{A[1]}], [{A[2]}]...[{A[-3]}], [{A[-2]}], [{A[-1]}]"

# =======================
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
# print(bubbleSort(A4))
# print(bubbleSort(A5))
print(bubbleSort(A6))