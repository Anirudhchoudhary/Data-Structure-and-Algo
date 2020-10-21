def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr


def rec_inserion(arr, i):
    if i == 0:
        return
    rec_inserion(arr, i-1)
    j = 0
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1

    return arr


if __name__ == "__main__":
    arr = [10, 32, 42, 53, 12, 531, 1, 431,
           431, 43124, 4312, 43215, 44, 532, 2]
    print(insertionsort(arr))
