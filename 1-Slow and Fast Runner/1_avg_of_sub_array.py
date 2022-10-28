from typing import List


def average_of_subarray(k, numns: List[int]):

    results = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(numns)):
        window_sum += numns[window_end]

        if window_end >= k-1:
            results.append(window_sum/k)
            window_sum -= numns[window_start]
            window_start += 1
    return results


if __name__ == "__main__":
    print(average_of_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
    # print(average_of_subarray(2, [3, 5, 2, 7, 4, 1, 8, 2]))



