# # linear search in a sorted matrix is a straightforward approach to find a target value. In a sorted matrix, each row and each column is sorted in ascending order. This property allows us to efficiently search for the target value. 
# # worst case notation for linear search in a sorted matrix is O(n*m), where n is the number of rows and m is the number of columns.
# # average case notation for linear search in a sorted matrix is O(n+m), where n is the number of rows and m is the number of columns.
# # best case notation for linear search in a sorted matrix is O(1), which occurs when the target value is found at the first checked position.
# binary search works 


# 74. Search a 2D Matrix

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true 
# arr =[]
# for r in m:
#     arr += r 
# l,ri = 0,len(arr)-1
# while l <= ri:
#     mid = (l+ri)//2
#     if t == arr[mid] :
#         return True
#     elif t < arr[mid]:
#         ri = mid - 1 
#     else: 
#         l = mid + 1 
# return False 



# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#       m = len(matrix)
#       n = len(matrix[0])
#       left = 0
#       rig = m*n-1
#       while left <= rig:
#         mid = (left+rig) // 2
#         ro,co = mid // n,mid % n 
#         if target == matrix[ro][co]:
#           return True 
#         elif target < matrix[ro][co]:
#           rig = mid -1 
#         else:
#           left = mid + 1 
#       return False


# 240. Search a 2D Matrix II
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m,n = len(matrix),len(matrix[0])
#         ro,co = 0,n-1
#         while ro < m and co >= 0:
#           if target ==  matrix[ro][co]:
#             return True 
#           elif target < matrix[ro][co]:
#             co -= 1
#           else:
#             ro += 1 
#         return False 

# 378