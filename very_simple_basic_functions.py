def return_sum_of_numbers(arr: list[int]) -> int:
    sumi = 0
    for number in arr:
        if number % 2 == 0:
            sumi += number
    return sumi

def check_is_palindrom(my_str: str) -> bool:
    return my_str == my_str[::-1]

def return_positive_numbers_in_array(arr: list[int]) -> list[int]:
    return [number for number in arr if number > 0]

def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    new_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    while i != len(arr1):
        new_arr.append(len(arr2))
        i += 1
    while j != len(arr2):
        new_arr.append(arr2[j])
        j += 1
    return new_arr

