# 1572
# 498
# 1380
# 1582

# len(mat) = no.of rows 
# len(mat[0]) = no.of columns 
# mat[r][c] we can get elements in that position 

# 1572. Matrix Diagonal Sum 

#  BRUTE :
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#       s = 0
#       for i in range(len(mat)):
#         for j in range(len(mat[0])):
#           if i == j or  i+j == len(mat)-1 :
#             s += mat[i][j] 
#       return s
# OPTIMIZED:
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#       s = 0
#       n = len(mat)
#       for i in range(n):
#         s += mat[i][i] 
#         s += mat[i][n-i-1]
#       if n % 2 == 1 :
#         s -= mat[n//2][n//2] 
#       return s

#498. Diagonal Traverse 
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#       ro , co = len(mat) , len(mat[0])
#       re = [] 
#       for d in range(ro+co-1):
#         dig = [] 
#         r = 0 if d < co else d - co + 1
#         c = d if d < co else co - 1 
#         while r < ro and c >= 0 :
#           dig.append(mat[r][c])
#           r += 1 
#           c -= 1 
#         if d % 2 == 0:
#           dig.reverse()
#         re += dig
#       return re
# # daigonels count = row + col - 1 


#1380. Lucky Numbers in a Matrix
# class Solution:
#     def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
#       mr = {min(r) for r in matrix}
#       mc = {max(c) for c in zip(*matrix)}
#       return list(mr & mc)

# #1582. Special Positions in a Binary Matrix
# class Solution:
#     def numSpecial(self, mat: List[List[int]]) -> int:
#         cs = [sum(c) for c in zip(*mat)]
#         rs = [sum(r) for r in (mat)] 
#         c = 0 
#         for i in range(len(mat)):
#           for j in range(len(mat[0])):
#             if mat[i][j] == 1 and rs[i] == 1 and cs[j] == 1:
#               c += 1 
#         return c