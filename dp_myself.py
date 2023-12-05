import time
import resource

# Referensi: https://www.geeksforgeeks.org/partition-problem-dp-18/

def partition_checker(arr_set):
    arr = list(arr_set)  # set di convert list ke  agar mempermudah iterasi :) (plis boleh dong)
    jumlah = sum(arr)
    if jumlah % 2 != 0:
        return False, set()

    target = jumlah // 2
    dp = {0: set()}

    for i in range(len(arr) - 1, -1, -1):
        new_dp = {}
        for t, subset in dp.items():
            if t + arr[i] == target:
                return True, subset.union({arr[i]})
            new_subset = subset.union({arr[i]})
            new_dp[t + arr[i]] = new_subset
            new_dp[t] = subset
        dp = new_dp

    return False, set()

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = {int(line.strip()) for line in file}  
    return numbers

dataset = ['dataset_kecil.txt', 'dataset_sedang.txt', 'dataset_besar.txt']

for i in range(3):
    input_set = read_numbers_from_file(dataset[i])
    n = len(input_set)
    start_time = time.time()
    success, subset = partition_checker(input_set)
    end_time = time.time()
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024


    if success:
        execution_time = (end_time - start_time) * 1000
        print(f"Running time for {dataset[i]}: {execution_time} milliseconds")
        print(f"Memory usage for {dataset[i]}: {memory_usage} bytes")
        print(f"Subset for {dataset[i]}: ")
        print(f"{subset} AND {(input_set - subset)}\n")
    
    else:
        print(f"Can't do it for {dataset[i]}")
