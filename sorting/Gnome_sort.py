def gnomesort(arr):
    i = 1
    while i < len(arr):
        if arr[i] > arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            if i == 1:
                i = 1
            else:
                i -= 1
        else:
            i += 1

    arr.reverse()
    return arr


if __name__ == "__main__":
    arr = [10, 32, 42, 53, 12, 531, 1, 431,
           431, 43124, 4312, 43215, 44, 532, 2]
    print(gnomesort(arr))
