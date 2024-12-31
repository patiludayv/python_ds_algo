def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_val:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = current_val

    return arr


if __name__ == '__main__':
    arr = [6, 5, 3, 1]
    print(insertion_sort(arr))
