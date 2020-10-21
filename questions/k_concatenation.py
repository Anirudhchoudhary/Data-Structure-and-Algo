'''
You are given an array A with size N (indexed from 0) and an integer K. 
Let's define another array B with size N · K as the array that's formed by concatenating K copies of array A.

For example, if A = {1, 2} and K = 3, then B = {1, 2, 1, 2, 1, 2}.

You have to find the maximum subarray sum of the array B. Fomally, 
you should compute the maximum value of Bi + Bi+1 + Bi+2 + ... + Bj, where 0 ≤ i ≤ j < N · K.

Input
The first line of the input contains a single integer T denoting the number of test cases. 
The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A0, A1, ..., AN-1.

Output
For each test case, print a single line containing the maximum subarray sum of B


Constraints
1 ≤ T ≤ 10
1 ≤ N ≤ 105
1 ≤ K ≤ 105
-10^6 ≤ Ai ≤ 10^6 for each valid i



Example
Input:

2
2 3
1 2
3 2
1 -2 1

Output:

9
2


'''


def max_subarray(arr):
    current_max = arr[0]
    max_subarray = arr[0]
    for num in arr[1:]:
        if current_max < 0:
            current_max = num
        else:
            current_max += num
        if current_max > max_subarray:
            max_subarray = current_max

    return max_subarray


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        A1 = list(map(int, input().split()))
        if len(A1) == N:
            B1 = A1 * K
            sum_max = max_subarray(B1)
        print(sum_max)
