import time
import resource
def partition_checker(arr):
    jumlah = sum(arr)
    if jumlah%2 != 0:
        return False
    dp = set()
    dp.add(0)
    target = jumlah //2
    for i in range(len(arr)-1,-1,-1):
        new_dp = set()
        for t in dp:
            if (t+arr[i]==target):
                return True
            new_dp.add(t+arr[i])
            new_dp.add(t)
        dp = new_dp
    return True if target in dp else False


def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers



dataset = ['dataset_kecil.txt','dataset_sedang.txt','dataset_besar.txt']

	
for i in range(3):
	input_list = read_numbers_from_file(dataset[i])
	n = len(input_list)
	start_time = time.time()
	if partition_checker(input_list) == True:
		end_time = time.time()
		memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
		execution_time = (end_time - start_time) * 1000
		print(f"Running time for {dataset[i]} {execution_time} ")
		print(f"Memory usage for {dataset[i]} {memory_usage} ")
	else:
		print(f"Cant do it for {dataset[i]}")
	
