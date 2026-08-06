##############################################################################################################################
# input = {12,45,63,20,96,25,10}
# output = {12,20,96,10}
##CODE 1:
# def even(l) :
#     r = []
#     for i in l:
#         if i % 2 == 0:
#             r.append(i)
#     return r 
#CODE 2 TWO POINTER APPROACH :
# l = list(map(int,input().split()))
# i = 0
# for j in range(len(l)):
#     if l[j] % 2 == 0:
#         l[i] = l[j]
#         i += 1 
# print(l[:i])
################################################################################################
# REVERSE STRING # 
# input = PYTHON 
# output = NOHTYP
# s = input().strip()
# l = list(s)
# left = 0 
# right = len(l) - 1
# while left < right :
#     l[left],l[right] =l[right],l[left]
#     left += 1 
#     right -= 1 
# print("".join(l))   
