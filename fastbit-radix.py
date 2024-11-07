import os
import pandas as pd
from timeit import timeit
import numpy as np

def fastbit_radix_sort(arr):

    max_num = max(arr)
    num_bits = int(max_num).bit_length()  

    output = np.zeros(len(arr), dtype=int)

    for i in range(0, num_bits, 8):  

        mask = (1 << 8) - 1  

        count = [0] * 256  

        for num in arr:
            count[(num >> i) & mask] += 1
        
        for j in range(1, 256):
            count[j] += count[j - 1]

        for num in reversed(arr): 
            output[count[(num >> i) & mask] - 1] = num
            count[(num >> i) & mask] -= 1

        arr[:] = output

    return arr

def load_excel_data(filepath, column_name):
    df = pd.read_excel(filepath)
    return df[column_name].dropna().astype(int).tolist()

def measure_sort_times(filepath, column_name):
    arr = load_excel_data(filepath, column_name)

    fastbit_time = timeit(lambda: fastbit_radix_sort(arr.copy()), number=10)

    print(f"Original Fastbit-Radix Sort Time: {fastbit_time:.6f} seconds")

file_path = 'D:\\SCHOOL\\New folder (3)\\algo.xlsx'
column_name = "Numbers1"

measure_sort_times(file_path, column_name)