# 1351. Count Negative Numbers in a Sorted Matrix

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#       n = len(grid)
#       c=0
#       for r in grid:
#         for co in r:
#           if co< 0:
#             c+=1 
#       return c  
 
# 832. Flipping an Image 

# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for r in image:
#             r.reverse()
#             for i in range(len(r)):
#                r[i] = 1 if r[i] == 0 else 0

#         return image

# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for r in image:
#             r.reverse()
#             for i in range(len(r)):
#                 r[i] = 1-r[i]

#         return image