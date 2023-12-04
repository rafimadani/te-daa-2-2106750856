def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers



dataset = ['dataset_kecil.txt','dataset_sedang.txt','dataset_besar.txt']

	
for i in range(3):
	input_list = read_numbers_from_file(dataset[i])
	print(input_list)
    