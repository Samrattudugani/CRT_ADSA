# 496

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    nm = {}
    s = []
    for n in nums2:
        while s and s[-1] < n:
            nm[s.pop()] = n
        s.append(n)
    while s:
        nm[s.pop()] = -1 
    return [nm[n]for n in nums1]




nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))

#901
