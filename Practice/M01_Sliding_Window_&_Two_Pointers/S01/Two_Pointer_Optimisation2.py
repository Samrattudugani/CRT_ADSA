# 26. Remove Duplicates from Sorted Array
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# n = list(map(int,input().split()))
# i = 0
# for j in range(1,len(n)): 
#     if n[i] != n[j]:
#         i+=1 
#         n[i] = n[j] 
        
# print(i+1)

# 27. Remove Element
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# n = list(map(int,input().split()))
# val = int(input())
# k = 0
# for i in range(1,len(n)):
#     if n[i] != val :
#         n[k] = n[i] 
#         k += 1 
# print(k)

# 167. Two Sum II - Input Array Is Sorted
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# def twop(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]

#         if current_sum == target:
#             return [left + 1, right + 1]  # 1-based indexing
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1

#     return []

# arr = list(map(int, input().split()))
# target = int(input())

# print(twop(arr, target))

# 977. Squares of a Sorted Array

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         ans = []

#         for i in nums:
#             ans.append(i * i)

#         ans.sort()
#         return ans 

