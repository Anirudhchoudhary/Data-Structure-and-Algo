from collections import defaultdict


def countsort(array, key=lambda x: x):
    A = defaultdict(list)
    B = []
    for i in array:
        A[key(i)].append(i)
    for k in range(min(A), max(A)+1):
        B.extend(A[k])


if __name__ == "__main__":
    arr = [10, 32, 42, 53, 12, 531, 1, 431,
           431, 43124, 4312, 43215, 44, 532, 2]
    countsort(arr)
