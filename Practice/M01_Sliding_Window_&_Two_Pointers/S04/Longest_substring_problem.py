# # 904. Fruit Into Baskets
# # Example 1:

# # Input: fruits = [1,2,1]
# # Output: 3
# # Explanation: We can pick from all 3 trees.

# def fib(f):
#     l = 0
#     c = 0
#     fr = {}
#     a = 0
#     for r in range(len(f)):
#         fr[f[r]] = fr.get(f[r],0)+1
#         while len(fr) > 2:
#             fr[f[l]] -= 1
#             if fr[f[l]] == 0:
#                 del fr[f[l]]
#             l+=1 
#         a = max(a,r-l+1)
#     return a 
# f = list(map(int,input().split()))
# print(fib(f))

# 3. Longest Substring Without Repeating Characters
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# 1208 

def lsb(n):
    l,a= 0 ,0
    d = set()
    for r in range(len(n)):
        while n[r] in d:
            
            d.remove(n[l]) 
            l += 1
        d.add(n[r]) 
        a = max(a,r-l+1)
    return a 
n = input().split()
print(lsb(n))