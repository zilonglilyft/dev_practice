class Solution:
    """
    1.  use binary search algo
    (1) generate a new list to store the (pos, value) pair
    (2) sort the list by the value
    (3) apply binary search logic on the sorted list to find the target - i for each iteration
    (4) the complexity is o(n*log(n))
    """
    def binary_search(self, li, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if li[mid][0] == target:
                return mid
            elif li[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_nums = [[num, i] for i, num in enumerate(numbers)]
        new_nums.sort(key = lambda x: x[0]) # these are the key to store the pos of the original list. create a new list, store the pos, and then sort by the value.
        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i+1, len(new_nums)-1, b)
            else:
                j = self.binary_search(new_nums, 0, i-1, b)
            if j:
                return [new_nums[i][1], new_nums[j][1]]