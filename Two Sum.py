
def twoSumNaive(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(f"Pair: {arr[i]} + {arr[j]}")



# Driver Code
arr = [5, 5, 2, 12, 3, 88]
target = 12

# Function call inside print
twoSumNaive(arr, target)