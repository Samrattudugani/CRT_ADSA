from typing import List

def productExceptSelf(arr: List[int]) -> List[int]:
    n = len(arr)
    res = [1] * n
    
    # Calculate prefix products for each element
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]
        
    # Multiply by suffix products from the right
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]
        
    return res

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))