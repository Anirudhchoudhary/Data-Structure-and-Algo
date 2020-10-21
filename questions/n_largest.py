'''
Problem statement :- Can You find the largest number in the array

example : [19,10,14,2,17,89,35,78,98,23,52]
ouput :- 98

example :- [1,2]
output = 2

example:- [2,5,19,43,53,51,61,41,80,78,12,31,79,213]
output = 213


'''


def partition(arr):
    pi, seq = arr[0], arr[1:]
    lo = [x for x in seq if x < pi]
    hi = [x for x in seq if x > pi]
    return lo, hi, pi


def largest(arr, s=None):
    pass


if __name__ == "__main__":
    arr = [2, 5, 19, 43, 53, 51, 61, 41, 80, 78, 12, 31, 79, 213]
    largest(arr)
