

def mergesort(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res


if __name__ == "__main__":
    arr = [10, 32, 42, 53, 12, 531, 1, 431,
           431, 43124, 4312, 43215, 44, 532, 2]
    print(mergesort(arr))
