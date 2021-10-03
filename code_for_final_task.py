data = {}
info = []
sorted_data = {}


def files(file_list):
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            str_counter = 0
            for line in file:
                str_counter += 1

        with open(file_name, 'r', encoding='utf-8') as file:
            info_file = file.read()
            x = {file_name: [int(str_counter), info_file]}
            data.update(x)


files(['1_new.txt', '2.txt', '3.txt'])


def sort():
    sorted_values = sorted(data.values())

    for i in sorted_values:
        for k in data.keys():
            if data[k] == i:
                sorted_data[k] = data[k]
                break


sort()

with open('4_final_task.txt', 'a+', encoding='utf-8') as file:
    for file_name, info_list in sorted_data.items():
        file.write(f'{file_name}\n{info_list[0]}\n{info_list[1]}\n')