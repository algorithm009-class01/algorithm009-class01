def remove_solution(nums):
    """Very baoli, basically iterate the entire list, since it is sorted, compare the ith
    element with the i-1th, if identical, remove and continue (array length changed)

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if len(nums) == 0:
        return 0
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.remove(nums[i - 1])
            continue
        i += 1
    return len(nums)


def double_pointer(nums):
    """Classic double pointer solution. Pointer one starts from the beginning of the list,
    pointer two starts from 1st place. Compare the value of two pointers, if they are not equal,
    we have found two different numbers, so increase pointer one by 1, and store the new value at
    nums[pointer_one] for next compare.

    pointer_one + 1 is the total number of different elements

    Time complexity: O(n)
    Space complexity: O(1)
    """
    length = len(nums)
    if length == 0:
        return 0
    k = 0
    for i in range(1, length):
        if nums[k] < nums[i]:
            k += 1
            nums[k] = nums[i]
    return k + 1


def groupby_solution(nums):
    """The operation of groupby is similar to uniq filter in Linux.
    This method calculates the keys for each element present in iterable, in this case iterable is a list. It
    returns key and iterable of grouped items. In this case we only care about the key. For example,
    groupbu([1, 1, 2]) will be (1->(1, 1), 2(1)). Because it is written in C, it is faster than double pointer.

    Time complexity: O(n)
    Space compexity: O(1)
    """
    from itertools import groupby
    i = 0
    for k, _ in groupby(nums):
        nums[i] = k
        i += 1
    return i


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return groupby_solution(nums)
