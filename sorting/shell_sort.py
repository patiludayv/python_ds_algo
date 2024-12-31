def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        current_val = arr[i]
        position = i

        while position >= gap and arr[position - gap] > current_val:
            # print(f'{arr[position - gap]} > {current_val}')
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = current_val


def shell_sort(arr):
    sublist_count = len(arr) // 2

    while sublist_count > 0:
        for start in range(sublist_count):
            print(f' gap_insertion_sort({arr}, {start}, {sublist_count})')
            gap_insertion_sort(arr, start, sublist_count)

        sublist_count = sublist_count // 2
    return arr


if __name__ == '__main__':
    arr = [6, 5, 3, 1]
    print(shell_sort(arr))
