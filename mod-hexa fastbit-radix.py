import os
import pandas as pd
from timeit import timeit
import numpy as np

def fastbit_radix_like_sort(arr):
    max_num = max(arr)
    max_nibbles = (max_num.bit_length() + 3) // 4  

    buckets = {i: [] for i in range(16)}
    sorted_arr = arr[:]
    
    for nibble_pos in range(max_nibbles):
       
        for i in range(16):
            buckets[i] = []

        for num in sorted_arr:
            nibble = (num >> (4 * nibble_pos)) & 0xF  
            buckets[nibble].append(num)

        index = 0
        for i in range(16):
            for num in buckets[i]:
                sorted_arr[index] = num
                index += 1

    return sorted_arr

def load_excel_data(filepath, column_name):
    df = pd.read_excel(filepath)
    return df[column_name].dropna().astype(int).tolist()

def measure_sort_times(filepath, column_name):
    arr = load_excel_data(filepath, column_name)

    fastbit_like_time = timeit(lambda: fastbit_radix_like_sort(arr.copy()), number=10)

    print(f"Modified Hexadecimal Fastbit-Radix Sort Time: {fastbit_like_time:.6f} seconds")

file_path = 'D:\\SCHOOL\\New folder (3)\\algo.xlsx'
column_name = "Numbers1"

measure_sort_times(file_path, column_name)