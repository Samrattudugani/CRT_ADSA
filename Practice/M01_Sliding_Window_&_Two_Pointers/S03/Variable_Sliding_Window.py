# WHEN TO USE A Variable Sliding Window approach:
# * LONGEST substring problems
# * Shortest substring problems
# Minimum
# At most K
# At least K
# Without repeating
# Distinct characters
# Sum >= target

###GENERAL STRUCTURE 
# left = 0
# answer = 0   # or float('inf'), depending on the problem

# for right in range(len(nums)):
#     # 1. Expand the window
#     # Include nums[right] or s[right]

#     while window_is_invalid:
#         # 2. Shrink the window
#         # Remove nums[left] or s[left]
#         left += 1

#     # 3. Update the answer
#     answer = max(answer, right - left + 1)
#     # or answer = min(answer, right - left + 1)

# return answer

# 209. Minimum Size Subarray Sum

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint. 

# def msar(t,n):
#     l = 0 
#     cs = 0
#     mil = float("inf")
#     for r in range(len(n)):
#         cs += n[r] 
#         while cs >= t:
           
#             mil = min(mil,r-l+1)
#             cs -= n[l] 
#             l += 1
#     return 0 if mil == float("inf") else mil 
# t = int(input())
# n = list(map(int,input().split()))
# print(msar(t,n))


# 713. Subarray Product Less Than K

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# def slk(n,k):
#     if k <= 1:
#         return 0 
#     l = 0
#     c = 0
#     pr = 1 
#     for r in range(len(n)):
#         pr *= n[r]
#         while pr >= k:
#             pr //= n[l]
           
#             l += 1
#         c += r-l+1 
#     return c 
# n = list(map(int,input().split()))
# k = int(input())
# print(slk(n,k)) 
