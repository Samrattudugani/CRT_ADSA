def countGoodSubstrings(s: str) -> int:
    count = 0
    # Slide a window of length 3 through the string
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]
        # Check if all 3 characters are distinct
        if a != b and b != c and a != c:
            count += 1
    return count

if __name__ == '__main__':
    s = input().strip()
    print(countGoodSubstrings(s))