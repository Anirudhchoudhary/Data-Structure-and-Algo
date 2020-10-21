import timeit


'''
QuickSort is a Divide and Conquer algorithm
you have to pick the pivot point
example arr= [10,4,1,5,8,9]
               ^
               |(This is the pivor point i am taking starting point as pivot point)
You can take the last or median or random index

complexity and other thing hear
Time Complexity of quicksort is

T(n) + T(K) + T(n-k-1) + O(n)

best case : O(nlogn)
worst Case  : O(n^2)
average Case : O(nlogn)

'''


def partition(arr):
    # selecting pivot point as starting index and rest the array to compare
    pi, seq = arr[0], arr[1:]
    # seprate the value less than the value of pivot point
    lo = [x for x in seq if x <= pi]
    # seprate the high value than the value of pivot point
    hi = [x for x in seq if x > pi]
    return pi, lo, hi


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pi, lo, hi = partition(arr)
    return quicksort(lo) + [pi] + quicksort(hi)


if __name__ == "__main__":
    mysetup = "from __main__ import quicksort"
    mystm = '''
arr = [10, 32, 42, 53, 12, 531, 1, 431,4389, 43124, 4312, 43215, 44, 532, 2]
quicksort(arr)
    '''
    import random
    arr = []
    for _ in range(1000):
        arr.append(random.randint(1, 1000))

    a = quicksort(arr)
    print(" The sorted array is", end=" ")
    print(a)
    # The sorted array is [1, 2, 10, 12, 32, 42, 44, 53, 431, 431, 531, 532, 4312, 43124, 43215]
    # times = timeit.repeat(setup=mysetup, stmt=mystm)
    # print("The time required to excetute the funtion is  ", min(times))
    # The time required to excetute the funtion is 12.850208602001658s
