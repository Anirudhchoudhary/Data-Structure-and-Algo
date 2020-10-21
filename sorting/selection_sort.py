
import timeit
import random
arr = []
for _ in range(1000):
    arr.append(random.randint(1, 1000))


def selectionsort(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(i, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == "__main__":
    selectionsort(arr)
    mysetup = '''
from __main__ import selectionsort
import random
    '''
    mystm = '''
arr = []
for _ in range(1000):
    arr.append(random.randint(1, 1000))
selectionsort(arr)
    '''
    # times = timeit.repeat(setup=mysetup, stmt=mystm)
    # print("The time required to excetute the funtion is  ", min(times))
    # The time required to excetute the funtion is   11.193549724999684
