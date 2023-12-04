import time
import resource

#referensi : https://www.geeksforgeeks.org/partition-problem-dp-18/

def partition_checker(arr):
    jumlah = sum(arr)
    if jumlah % 2 != 0:
        return False, []

    target = jumlah // 2
    dp = {0: []}

    for i in range(len(arr) - 1, -1, -1):
        new_dp = {}
        for t, subset in dp.items():
            if (t + arr[i] == target):
                return True, subset + [arr[i]]
            new_subset = subset + [arr[i]]
            new_dp[t + arr[i]] = new_subset
            new_dp[t] = subset
        dp = new_dp
    print("anji")

    return False, []

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

dataset = ['dataset_kecil.txt', 'dataset_sedang.txt', 'dataset_besar.txt']

for i in range(3):
    input_list = read_numbers_from_file(dataset[i])
    n = len(input_list)
    start_time = time.time()
    success, subset = partition_checker(input_list)
    end_time = time.time()
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    subset2 = []

    element_counts = {}
    for num in input_list:
        if num in element_counts:
            element_counts[num] += 1
        else:
            element_counts[num] = 1

    for num in subset:
        if element_counts[num] > 0:
            element_counts[num] -= 1

    for num, count in element_counts.items():
        if count > 0:
            for _ in range(count):
                subset2.append(num)

    if success:
        execution_time = (end_time - start_time) * 1000
        print(f"Running time for {dataset[i]}: {execution_time} milliseconds")
        print(f"Memory usage for {dataset[i]}: {memory_usage} bytes")
        print(f"Subset for {dataset[i]}: {subset} AND {subset2}")
    else:
        print(f"Can't do it for {dataset[i]}")
