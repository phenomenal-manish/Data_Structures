# Problem Statement: Find maximum subarray sum 

def kadane(arr):
    curr_sum = 0
    max_sum = 0

    for idx in range(len(arr)):
        curr_sum += arr[idx]

        max_sum = max(max_sum, curr_sum)

        # Check if current sum becomes negative, start over again
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


A = [1, -2, -3, 4, -1, 2, 1] 
# A = [-1, 2, -2, 5, 7, -3, 1]
print("Maximum Subarray Sum: ", kadane(A))