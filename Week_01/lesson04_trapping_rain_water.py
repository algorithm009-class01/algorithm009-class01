def sum_water_by_row(height):
    """Calculate the sum water by row. The maximum number of row is the max height.
    for h in max(1, height+1):
        for i in (len(height)):
            temp_sum = 0
            update_sum = False
            if height[i] < h and update_sum:
                temp_sum += 1
            if height[i] >= h:
                add temp_sum to total
                set temp_sum to 0
                set update_sum to True
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    if len(height) == 0:
        return 0
    max_h = max(height)
    total_sum = 0
    for h in range(1, max_h + 1):
        temp_sum = 0
        update_sum = False
        for i in range(len(height)):
            # There is room for trapping water
            if height[i] < h and update_sum:
                temp_sum += 1
            if height[i] >= h:
                total_sum += temp_sum
                temp_sum = 0
                update_sum = True
    return total_sum


def sum_water_by_column(height):
    """Iterate each column, and calculate the sum water.
    We can skip the left most and right most column, because they can hold 0 amount of water
    For each column, the amount of water it can hold is
        amount = min(left_max_height, right_max_height) - column_height
        if amount <= 0, no water can be hold
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    total_sum = 0
    for i in range(1, len(height) - 1):
        # Find the left max
        lm = max(height[:i])
        # Find the right max
        rm = max(height[i + 1:])

        if min(lm, rm) - height[i] > 0:
            total_sum += min(lm, rm) - height[i]
    return total_sum


def sum_water_by_column_dynamic(height):
    """This solution is a variant of sum_water_by_column.
    Instead of find left_max and right_max for each i, in the for loop, which makes the time complexity
    to O(n^2), we can pre-calculate the left_max and right_max for each i and save them into two lists.

    lm[i]: list that stores left_max height for index i
    rm[i]: list that stores right_max height for index i

    Then the amount of water that column i can hold is the min(lm[i], rm[i]) - height[i]
    Time complexity: O(n)
    Space complexity: O(3n)
    """
    total_sum = 0
    lm = [0] * len(height)
    rm = [0] * len(height)
    # For each i, calculate left_max, we don't need to consider index 0
    for i in range(1, len(height) - 1):
        # Since lm[i-1] is already the left_max, we only need to compare with height[i-1]
        lm[i] = max(lm[i - 1], height[i - 1])

    # For each i, calculate right_max, we don't need to consider index length-1
    for i in range(len(height) - 2, -1, -1):
        rm[i] = max(rm[i + 1], height[i + 1])

    for i in range(len(height) - 1):
        temp = min(lm[i], rm[i])
        if temp - height[i] > 0:
            total_sum = total_sum + (temp - height[i])

    return total_sum


class Solution:
    def trap(self, height: List[int]) -> int:
        return sum_water_by_column_dynamic(height)
