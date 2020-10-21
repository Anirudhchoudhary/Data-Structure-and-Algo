from collections import defaultdict


def countsort(arr, place, key=lambda x: x % 10):
    A, B = defaultdict(list), []
    for i in arr:
        index = i // place
        A[key(index)].append(i)
    for i in range(min(A), max(A)+1):
        B.extend(A[i])

    return B


def radix_sort(arr):
    m = max(arr)
    place = 1
    n = arr
    while m // place > 0:
        n = countsort(n, place)
        place *= 10

    print(n)


if __name__ == "__main__":
    arr = [10, 32, 42, 53, 12, 531, 1, 431,
           431, 43124, 4312, 43215, 44, 532, 2]
    radix_sort(arr)
