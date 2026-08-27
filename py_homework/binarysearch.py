def bsearch(L, target):
    lo, hi = 0, len(L) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if L[mid] == target: return mid
        if L[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1

s=[2,3,5,11,15,16]
print(bsearch(s,5)+1)