from typing import List

def pairInSortedRotated(arr: List[int], target: int) -> bool:
    n = len(arr)
    if n < 2:
        return False
    
    # Find the pivot point (index of the maximum element)
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break
            
    # 'l' points to smallest element, 'r' points to largest element
    l = (pivot + 1) % n
    r = pivot
    
    # Standard two-pointer logic with modular arithmetic for rotation
    while l != r:
        current_sum = arr[l] + arr[r]
        if current_sum == target:
            return True
        elif current_sum < target:
            l = (l + 1) % n
        else:
            r = (r - 1 + n) % n
            
    return False

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))