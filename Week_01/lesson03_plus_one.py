def method_str_int_convert(nums):
    """Method one, use string <-> int conversion
    1. Convert string to int, using map function
    2. Plus one to int
    3. Convert int back to string

    Time complexity: O(n)
    Space complexity: n
    """
    n = int(''.join(map(str, nums))) + 1
    # Convert int back to str
    str_n = [int(x) for x in str(n)]
    return str_n


def method_recursive(digits):
    """Method two, use recursive
    1. Check the last digit, if less than 9, simply plus one
    2. Handle the simple use case when digits = [9
    3. Recursive on digits[0:-1]

    Time complexity: O(n)
    Space complexity: n
    """
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = self.plusOne(digits[0:-1])
        return digits


def method_loop(digits):
    """Method three, use while loop
    1. Insert 0 at the begining, in case we have [9, 9..]
    2. Check last digit, if less than 9, simply plus one
    3. If the last digit is 9, set it to 0, and add carry

    Time complexity: O(n)
    Space complexity: n
    """
    digits.insert(0, 0)
    # Loop through the list from the end
    i = len(digits) - 1
    while i >= 0:
        # If the digit is less than 9, just plus one
        if digits[i] < 9:
            digits[i] += 1
            break
        else:
            # Set digit to 0, and leaev the carry to the next lopp iteration
            digits[i] = 0
            i -= 1
    if digits[0] == 0:
        digits.pop(0)
    return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return method_str_int_convert(digits)
