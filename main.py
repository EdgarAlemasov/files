from pprint import pprint

cook_book = {}
with open('recipe_list.txt', encoding='utf-8') as file:
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())

        temp_list = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp_list.append(
                {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure}
            )

        cook_book[dish_name] = temp_list

        file.readline()


def get_shop_list_by_dishes(dish, person_count):
    shop_list = {}
    for dishes, list in cook_book.items():
      for info in list:
        for name in dish:
          if name in dishes:
            count = info['quantity'] * person_count
            info_key = f"{info['ingredient_name']}"
            if info['ingredient_name'] in shop_list:
                count += count
                info_values = f"quantity : {count}, measure : {info['measure']}"
                x = {info_key: {info_values}}
                shop_list.update(x)
            else:
                pass
            info_values = f"quantity : {count}, measure : {info['measure']}"
            x = {info_key: {info_values}}
            shop_list.update(x)
          else:
            continue
    pprint(shop_list)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
