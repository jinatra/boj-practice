class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        # [-4, -1, 1, 2] / target = 1
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # 합
                total = nums[i] + nums[left] + nums[right]
                # total = 2 / closest = 2
                # 합이 타겟이랑 같으면 답
                if total == target:
                    return total
                
                # 현재 합과의 차가 더 작으면 바꾸기
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                # 현재합이 더 작으면 값 키우기
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return closest