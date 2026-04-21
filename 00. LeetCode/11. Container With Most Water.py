class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 인덱스 (너비)
        left = 0
        right = len(height) - 1
        
        # 짧은거를 한칸 이동
        max_area = 0
        while left < right:
            # 영역
            area = min(height[left], height[right]) * (right - left)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            # 무게 비교
            max_area = max(max_area, area)
        
        return max_area