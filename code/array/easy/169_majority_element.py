from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = self.find_candidate(nums)

        if candidate is None or not self.verify(nums, candidate):
            return -1
        
        return candidate
        
    

    def find_candidate(self, nums: List[int]):

        candidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if candidate == num:
                count += 1

            else:
                count -= 1

        return candidate
    

    def verify(self, nums: List[int], candidate: int):
        cnt = 0

        for num in nums:
            if candidate == num:
                cnt +=1 

        return cnt > len(nums) // 2