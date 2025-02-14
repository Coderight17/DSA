def merge(arr, low, mid, high):
    i = low
    j = mid+1
    t = []
    count = 0
    while i<=mid and j<=high:
        if arr[i]> arr[j]:
            count = count + mid-i+1
            t.append(arr[j])
            j = j+1
        else:
            t.append(arr[i])
            i = i+1
    while i<=mid:
        t.append(arr[i])
        i = i+1
    while j<= high:
        t.append(arr[j])
        j = j+1
    for k in range(low, high+1):
        arr[k] = t[k-low]
    return count
def mergesort(arr, low, high):
    count = 0
    if low < high:
        mid = int((low+high)//2)
        count = count + mergesort(arr, low, mid)
        count = count + mergesort(arr, mid+1, high)
        count = count + merge(arr, low, mid, high)
    return count
def getInversions(arr, n):
    count = mergesort(arr, 0, n-1)
    return count
