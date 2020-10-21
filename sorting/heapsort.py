import heapq as heap


def heapsort(arr):
    heap.heapify(arr)
    output = []
    for _ in range(len(arr)):
        n = heap.heappop(arr)
        output.append(n)

    return output


if __name__ == "__main__":
    arr = [10, 32, 42, 53, 12, 531, 1, 431,
           431, 43124, 4312, 43215, 44, 532, 2]
    heapsort(arr)
