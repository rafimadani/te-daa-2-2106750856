import time
import resource

def is_subset_sum(arr, n, target_sum, current_sum, index, selected):
    if current_sum == target_sum:
        print(index)
        return True
    
    if index == n or current_sum > target_sum:
        return False

    selected[index] = True
    if is_subset_sum(arr, n, target_sum, current_sum + arr[index], index + 1, selected):
        return True

    selected[index] = False
    if is_subset_sum(arr, n, target_sum, current_sum, index + 1, selected):
        return True

    return False

def anonymous_function(arr):
    n = len(arr)
    total_sum = sum(arr)

    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    selected = [False] * n

    return is_subset_sum(arr, n, target_sum, 0, 0, selected)



def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers



dataset = ['dataset_kecil.txt','dataset_sedang.txt','dataset_besar.txt']

	
for i in range(3):
	input_list = read_numbers_from_file(dataset[i])
	n = len(input_list)
    
	start_time = time.time()
	if anonymous_function(input_list) == True:
		end_time = time.time()
		memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
		execution_time = (end_time - start_time) * 1000
		print(f"Running time for {dataset[i]} {execution_time} ")
		print(f"Memory usage for {dataset[i]} {memory_usage} ")
	else:
		print(f"Cant do it for {dataset[i]}")

