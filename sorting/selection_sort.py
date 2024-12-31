def selection_sort(arr):
    for fill_slot in range(len(arr) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location

        temp = arr[fill_slot]
        arr[fill_slot] = arr[position_of_max]
        arr[position_of_max] = temp

    return arr


if __name__ == '__main__':
    arr = [6, 5, 3, 1]
    print(selection_sort(arr))
