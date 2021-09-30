from pprint import pprint


def data_file(file_name):
    cook_book = {}
    with open(file_name) as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                )

            cook_book[dish_name] = temp_list

            file.readline()

    return cook_book


pprint(data_file('recipe_list.txt'))
