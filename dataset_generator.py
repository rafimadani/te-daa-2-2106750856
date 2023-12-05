import random

def generate_dataset(size):
    unique_numbers = set()

    while len(unique_numbers) < size:
        unique_numbers.add(random.randint(1, 500) * 2)

    return list(unique_numbers)

def save_to_txt(filename, dataset):
    with open(filename, 'w') as file:
        for number in dataset:
            file.write(str(number) + '\n')

# Kecil (list dengan 10 angka random)
dataset_kecil = generate_dataset(10)
save_to_txt('dataset_kecil.txt', dataset_kecil)

# Sedang (list dengan 40 angka random)
dataset_sedang = generate_dataset(40)
save_to_txt('dataset_sedang.txt', dataset_sedang)

# Besar (list dengan 80 angka random)
dataset_besar = generate_dataset(80)
save_to_txt('dataset_besar.txt', dataset_besar)
