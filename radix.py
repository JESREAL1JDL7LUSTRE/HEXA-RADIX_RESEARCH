import os
import pandas as pd
from timeit import timeit
import numpy as np

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  
    count = [0] * 10  

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):  
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):

    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def load_excel_data(filepath, column_name):
    df = pd.read_excel(filepath)
    return df[column_name].dropna().astype(int).tolist()

def measure_sort_times(filepath, column_name):
    arr = load_excel_data(filepath, column_name)

    radix_time = timeit(lambda: radix_sort(arr.copy()), number=10)

    print(f"Radix Sort Time: {radix_time:.6f} seconds")

file_path = 'D:\\SCHOOL\\New folder (3)\\algo.xlsx' 
column_name = "Numbers1"  

measure_sort_times(file_path, column_name)
