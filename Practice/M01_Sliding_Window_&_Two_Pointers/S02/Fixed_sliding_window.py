# SLIDING WINDOW 
# # 643. Maximum Average Subarray I
# from typing import List
# def findMaxAverage(self, nums:  List[int], k: int) -> float:
#     ms = -10000000000000
#     for i in range(len(nums) - k +1):
#         ws = 0 
#         for j in range(i,i+k):
#             ws += nums[j]
#             ms = max(ms,ws) 
#     return ms/k

# def fsd(l, k):
#     ws = sum(l[:k])
#     ms = ws

#     for i in range(k, len(l)):
#         ws += l[i]
#         ws -= l[i - k]
#         ms = max(ms, ws)

#     return ms / k
# l = list(map(int, input().split()))
# k = int(input())

# print(fsd(l, k))

# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have 
# averages less than 4 (the threshold).

# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

s = input().strip()
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {'a','e','i','o','u'}
        c = 0 
        
        for i in range(k):
            if s[i] in vow:
                c += 1 ;
        mx = c
        for i in range(k,len(s)):
            if s[i] in vow:
                c+= 1 
            if s[i-k] in vow:
                c -= 1 
            if c > mx:
                mx = c 
        return mx
