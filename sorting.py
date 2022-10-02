import random

# arr = [9, 3, 2, 4, 8, 1, 6]
# 1 # sort method
# arr.sort()
# print(arr)


def sort_bubble_sort(arr: list, reverse: bool = False) -> list:
    # 1 # bubble_sort O(n^^2):
    indexes = len(arr)
    for i in range(indexes - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            sort_bubble_sort(arr)

    if reverse:
        return arr[::-1]

    return arr


# print(sort_bubble_sort(arr))


def generate_n_four_digits_arr(n: int) -> list:
    arr = [(random.randint(999, 9999)) for _ in range(n)]
    # for _ in range(n):
    #     arr.append(random.randint(1000, 9999))
    return arr


if __name__ == '__main__':
    n = input("type int 0-20: ")
    arr = generate_n_four_digits_arr(int(n))
    print(arr)
    print(f'arr sorted with bubble sort: ')
    print(sort_bubble_sort(arr))
