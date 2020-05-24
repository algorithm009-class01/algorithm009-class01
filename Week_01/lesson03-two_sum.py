def double_loop(l, t):
    """Calculate all the possible combinations with a double loop
    Then compare the sum with target, if equal, return

    Time complexity: O(n)
    Space complextity: n

    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def hash_lookup(nums, target):
    """Use a hashmap to keep the value (key) <-> index(value) pair. The key of the hashmap
    would be target - nums[i], and index will be i. For example, for list [2, 7, 11, 15], and
    target 9, the hashmap will look like: {7:0, 2:1, -2:2, -6:3}. When we iterate the nums list,
    if there is a solution, the target-nums[i] would be already captured in the hashmap.

    For example, nums[0] = 2, and target - nums[0] = 7, so hashmap is {7:0}, then when
    we move to nums[1] which is 7, the hashmap would already have key 7, which means there is
    a solution.
    """
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            return [d[nums[i]], i]
        d[target - nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return hash_lookup(nums, target)
