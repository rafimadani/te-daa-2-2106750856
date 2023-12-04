import time
import resource

def is_subset_sum(arr, n, target_sum, current_sum, index, selected, subset1, subset2):
    if current_sum == target_sum:
        # Extract subsets
        for i in range(n):
            if selected[i]:
                subset1.append(arr[i])
            else:
                subset2.append(arr[i])
        return True
    
    if index == n or current_sum > target_sum:
        return False

    selected[index] = True
    if is_subset_sum(arr, n, target_sum, current_sum + arr[index], index + 1, selected, subset1, subset2):
        return True

    selected[index] = False
    if is_subset_sum(arr, n, target_sum, current_sum, index + 1, selected, subset1, subset2):
        return True

    return False

def branch_and_bound(arr):
    n = len(arr)
    total_sum = sum(arr)

    if total_sum % 2 != 0:
        return False, [], []

    target_sum = total_sum // 2
    selected = [False] * n
    subset1 = []
    subset2 = []

    result = is_subset_sum(arr, n, target_sum, 0, 0, selected, subset1, subset2)

    return result, subset1, subset2

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

dataset = ['dataset_kecil.txt', 'dataset_sedang.txt', 'dataset_besar.txt']

for i in range(3):
    input_list = read_numbers_from_file(dataset[i])
    n = len(input_list)

    start_time = time.time()
    success, subset1, subset2 = branch_and_bound(input_list)
    end_time = time.time()
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    execution_time = (end_time - start_time) * 1000

    if success:
        print(f"Running time for {dataset[i]}: {execution_time} milliseconds")
        print(f"Memory usage for {dataset[i]}: {memory_usage} bytes")
        print("Subset 1:", subset1)
        print("Subset 2:", subset2)
    else:
        print(f"Cannot divide the list into two equal subsets for {dataset[i]}")
