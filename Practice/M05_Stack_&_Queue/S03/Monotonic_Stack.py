# '''

# Two TYPES OF MONOTONIC STACK :
# 1.INCREASNG MONO STACK 
# EX: 1,3,5,7

# GENERAL CODE:
# stack = [] 
# for x in arr:
#     while stack and stack[-1] > x:
#         stack.pop()
#     stack.append(x)

# Monotonic Increasing stack:
# stack = []
# for x in arr:
#     while stack and stack[-1] < x:
#         stack.pop()
#     stack.append(x)


# def get_monotonic_stack(arr):
#     stack = []
#     for x in arr:
      
#         while stack and stack[-1] > x:
#             stack.pop()
#         stack.append(x)
#     return stack

# arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
# result = get_monotonic_stack(arr)
# print(result)

# def get_monotonic_stack(arr):
#     stack = []
#     for x in arr:
      
#         while stack and stack[-1] < x:
#             stack.pop()
#         stack.append(x)
#     return stack

# arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
# result = get_monotonic_stack(arr)
# print(result)
# '''
# # Next Greater Element
def nge(arr):
    n = len(arr)
    r = [0] * n 
    s = [] 
    for i in range(n-1,-1,-1):
        while s and s[-1] <= arr[i]:
            s.pop()
        r[i] = -1 if not s else s[-1]
        s.append(arr[i])
    return r

arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
print(nge(arr))













    
arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
result = nge(arr)
print(result)
