class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, first_num in enumerate(nums):
            second_num = target - first_num
            if second_num in nums:
                for index_2, element in enumerate(nums):
                    if second_num == element and index_1 != index_2:
                        ans = [index_1, index_2]
                        ans.sort()
                        return ans