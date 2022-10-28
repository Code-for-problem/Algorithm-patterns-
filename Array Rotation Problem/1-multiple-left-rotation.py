"""
Given an array of size n and multiple values around which we need to
left rotate the array.How to quickly find multiple left rotations?

Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 1
        k2 = 3
        k3 = 4
        k4 = 6
Output : 3 5 7 9 1
         7 9 1 3 5
         9 1 3 5 7
         3 5 7 9 1

Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 14
Output : 9 1 3 5 7
"""

from typing import List


def multiple_left_rotation(numns: List[int], k: int):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(numns)
    k %= n
    return numns[k:] + numns[:k]


if __name__ == "__main__":
    print(multiple_left_rotation([1, 3, 5, 7, 9], 1) == [3, 5, 7, 9, 1])
    print(multiple_left_rotation([1, 3, 5, 7, 9], 3) == [7, 9, 1, 3, 5])
    print(multiple_left_rotation([1, 3, 5, 7, 9], 4) == [9, 1, 3, 5, 7])
    print(multiple_left_rotation([1, 3, 5, 7, 9], 6) == [3, 5, 7, 9, 1])
    print(multiple_left_rotation([1, 3, 5, 7, 9], 14) == [9, 1, 3, 5, 7])


