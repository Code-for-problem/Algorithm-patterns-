
def max_subarray_of_size_k(k, numns: list):
    """
    Given an array of positive numbers and a positive number ‘k’,
    find the maximum sum of any contiguous subarray of size ‘k’.
    e-g:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
    """
    k_sum = sum(numns[:k])
    max_sum = k_sum
    window_start = 0

    for window_end in range(k, len(numns)):
        k_sum += numns[window_end] - numns[window_start]
        max_sum = max(max_sum, k_sum)
        window_start += 1
    return max_sum


if __name__ == "__main__":
    print(max_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_subarray_of_size_k(2, [2, 3, 4, 1, 5]))