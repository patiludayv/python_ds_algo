def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp

    return arr


if __name__ == '__main__':
    arr = [6, 5, 3, 1]
    print(bubble_sort(arr))
