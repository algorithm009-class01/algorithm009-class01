def module_solution(nums, k):
    """Iterate the entire list from index 0, use module method to calculate the
    new index. The relationship betweek array length, k and index is:
    i = (length-k+i)%length

    Time complexity: O(n)
    Space complexity: O(n)
    """
    length = len(nums)
    nums2 = list(nums)
    for i in range(length):
        nums[i] = nums2[(length - k + i) % length]


def list_slice(nums, k):
    """Use list slice, rotate by k means slice the list from -k to the end, and
    place the slice in front of the list

    Time complexity: O(1)
    Space complexity: O(n)
    """
    length = len(nums)
    new_index = k % length
    if new_index == 0:
        return
    nums[:new_index], nums[new_index:] = nums[-new_index:], nums[:length - new_index]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list_slice(nums, k)
