# #1480 
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#       l = 0
#       a = []
#       for r in range(len(nums)):
#         l += nums[r]
#         a.append(l) 
#       return a

# #1732
# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#       l=0
#       a = [0]
#       for i in range(len(gain)):
#         l += gain[i] 
#         a.append(l) 
#       return max(a)
