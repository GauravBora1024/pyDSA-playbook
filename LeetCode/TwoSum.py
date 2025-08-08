# O(n) 
'''
Using the algo for hashmaps 

So the algorithm is basically:
- For each number, calculate the complement.
- Check if the complement is already in your memory (hashmap).
- If yes, return their positions.
- If no, stash the current number and keep going.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
        return []
    




# with O(n2) - brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               if nums[i]+nums[j] == target:
                    return [i, j]