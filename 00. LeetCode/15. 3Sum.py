class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # 중복 1: 같은 first 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            first = nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = first + nums[left] + nums[right]
                if total == 0:
                    ans.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 중복 2: 같은 값 건너뛰기
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans