

def window_sum(k, nums):
    # sum of the first k elements
    k_sum = sum(nums[:k])
    window_start = 0
    results = [k_sum]
    for window_end in range(k, len(nums)):
        k_sum += nums[window_end] - nums[window_start]
        results.append(k_sum)
        window_start += 1

    return results


if __name__ == "__main__":
    print(window_sum(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
