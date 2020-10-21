def bucketSort(array):
    bucket = []
    for i in range(len(array)):
        bucket.append([])

    for i in array:
        j = int(10 * i)
        bucket[j].append(i)

    for i in bucket:
        i = i.sort()

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1

    return array


if __name__ == "__main__":
    array = [.42, .32, .33, .52, .37, .47, .51]
    print("Sorted Array in descending order is")
    print(bucketSort(array))
