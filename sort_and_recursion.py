def sum_digits_of_number(number: int) -> int:
    if number == 0:
        return 0

    return sum_digits_of_number(number // 10) + number % 10

# def bubble_sort(arr: list[int]) -> None:
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort(arr: list[int], length: int = None):
    if length is None:
        length = len(arr) - 1

    if length <= 1:
        return

    for i in range(length):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort(arr, length - 1)


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def merge(arr1: list[int], arr2: list[int]):

    new_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        new_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        new_arr.append(arr2[j])
        j += 1

    return new_arr

def merge_sort(arr: list[int]):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def selection_sort(arr: list[int], sorted_idx: int = 0):

        if sorted_idx == len(arr):
            return

        smallest_idx = sorted_idx
        for i in range(sorted_idx,  len(arr)):
            if arr[smallest_idx] > arr[i]:
                smallest_idx = i

        arr[sorted_idx], arr[smallest_idx] = arr[smallest_idx], arr[sorted_idx]
        selection_sort(arr, sorted_idx + 1)

def binary_search(arr: list[int], target: int, counter: int = 0) -> int:
    if not arr:
        return -1

    mid = len(arr) // 2
    if arr[mid] == target:
        return mid + counter

    if arr[mid] > target:
        return binary_search(arr[:mid], target, counter)
    else:
        return binary_search(arr[mid + 1:], target, counter + mid + 1)

arr = [32, 12, 23, 1, 32, 54, 24, 255, 2]

def linear_search(arr: list[int], target: int, counter: int = 0) -> list[int]:

    if not arr:
        return []

    if arr[0] == target:
        return [counter] + linear_search(arr[1:], target, counter + 1)
    return linear_search(arr[1:], target, counter + 1)

def get_unsorted_array(arr: list[int], mini: int = None, maxi: int = None):

    if not arr:
        return mini, maxi

    if mini is None and maxi is None:
        mini = maxi = arr[0]

    if arr[0] < mini:
        mini = arr[0]

    if arr[0] > maxi:
        maxi = arr[0]

    return get_unsorted_array(arr[1:], mini, maxi)


def get_sorted_array(arr: list[int], target: int) -> int:

    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right)  // 2

        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

def get_s(arr: list[int], target: int, left: int = 0, right: int = None):

    if right is None:
        right = len(arr)

    if left > right:
        return left

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return get_s(arr, target, left, mid - 1)
    else:
        return get_s(arr, target, mid + 1, right)

def filter_array_by_greater_than_power_of_2(arr: list[int], value: int) -> list[int]:
    return [number for number in arr if number > value ** 2]

def return_long_string(my_str: str) -> str:

    result = []

    start = 0
    for i in range(len(my_str)):
        if my_str[i] == " ":
            result.append(my_str[start:i])
            start = i + 1

    if my_str[-1] != " ":
        result.append(my_str[start:])

    return max(result, key=lambda k: len(k))

def return_common_elements_in_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    return [item for item in arr1 if item in arr2]

def return_sum_of_divisors(num: int) -> int:
    sumi = 0
    for i in range(num - 1, 0, -1):
        if num % i == 0:
            sumi += i
    return sumi

def return_dict_of_strings(arr: list[str]) -> dict:
    my_dict = {}
    for item in arr:
        if len(item) in my_dict:
            my_dict[len(item)].append(item)
        else:
            my_dict[len(item)] = [item]
    return my_dict

def get_two_arrays(arr1: list[int], arr2: list[int], k: int) -> bool:
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] + arr2[j] == k:
                return True
    return False

def return_most_letter_in_a_string(my_str: str) -> str:
    if not my_str:
        return ""

    my_dict = {}
    sumi = 0
    max_char = my_str[0]
    for i in range(len(my_str)):
        if my_str[i] not in my_dict:
            my_dict[my_str[i]] = 1
        else:
            my_dict[my_str[i]] += 1
        if my_dict[my_str[i]] > sumi:
            sumi = my_dict[my_str[i]]
            max_char = my_str[i]

    return max_char

def return_idx_of_the_nearest_average(arr: list[int]) -> int:

    if not arr:
        return -1

    average = sum(arr) / len(arr)
    idx = 0
    for i in range(1, len(arr)):
        if abs(average - arr[i]) < abs(average - arr[idx]):
            idx = i

    return idx

def remove_duplicates(arr: list[int]) -> list[int]:

    i = 0
    while i < len(arr):
        if arr[i] in arr[i + 1:]:
            arr.pop(i)
        else:
            i += 1
    return arr

def check_sorted_list(arr: list[int]):
    if len(arr) <= 1:
        return True

    if arr[0] > arr[1]:
        return False

    return check_sorted_list(arr[1:])

def change_odd_and_even(arr: list[int]) -> None:

    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] % 2 != 0:
            i += 1
        elif arr[j] % 2 == 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

# def find_combinations(num: int, target: int = None, result: list[list[int]] = []) -> list[list[int]]:
#     if target is None:
#         target = num
#
#     if num == 0:
#         return result
#     temp = []
#     for i in range(num, 0, -1):
#         temp.append(i)
#         if sum(temp) == target:
#             result.append(temp)
#             temp.pop()
#
#     find_combinations(num - 1, target, result)
#
#     return result


def find_combinations(num: int, target: int = None, temp: list[int] = None, result: list[list[int]] = None) -> list[list[int]]:

    if temp is None:
        temp = []

    if result is None:
        result = []

    if target is None:
        target = num

    if target == 0:
        result.append(temp[:])
        return result

    for i in range(num, 0, -1):
        if i <= target:
            temp.append(i)
            find_combinations(i, target - i, temp, result)
            temp.pop()

    return result

def sort_array_by_length(arr: list[str]) -> None:

    my_dict = {chr(i): i for i in range(65, 91)}
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif len(arr[j]) == len(arr[j + 1]):
                num_of_j = sum(my_dict[num] for num in arr[j].upper())
                num_of_next_j = sum(my_dict[num] for num in arr[j + 1].upper())
                if num_of_j > num_of_next_j:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr_of_strings = ["this", "is", "crazy", "now", "why", "that", "happening"]
sort_array_by_length(arr_of_strings)


def get_an_array(arr: list[int], k: int) -> list[int]:
    return arr[:].sort()[-k:]

def get_longest_subarray(arr: list[int]) -> list[int]:

    if not arr:
        return []

    current_sum = max_sum = arr[0]
    current_start = current_end = 0
    max_start = max_end = 0

    for i in range(len(arr)):
        if current_sum + arr[i] < 0:
            current_start = i + 1
            current_sum = 0
        else:
            current_sum += arr[i]
            current_end = i

        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = current_end


    return arr[max_start: max_end + 1]

print(get_longest_subarray([-11, 2, 3, 10, 1]))
