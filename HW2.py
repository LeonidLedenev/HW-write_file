import os
from pprint import pprint

def make_cook_book():
    path = os.path.join(os.getcwd(), 'recipe.txt')
    cook_book = {}
    with open(path, 'r', encoding='utf8') as recipes:
        for line in recipes:
            dish_name = line.strip()
            cook_book[dish_name] = []
            ingredient_count = recipes.readline()
            for parts in range(int(ingredient_count)):
                recipes_list = recipes.readline()
                ingredient_name, quantity, measure = recipes_list.split(' | ')
                dish_ingridient = {'ingredient_name': ingredient_name,
                                        "quantity": int(quantity),
                                        "measure": measure.strip()}
                cook_book[dish_name].append(dish_ingridient)
            recipes.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredient in cook_book[dish_name]:
                shop_list = {}
                if ingredient['ingredient_name'] not in ingredient_list:
                    shop_list['measure'] = ingredient['measure']
                    shop_list['quantity'] = ingredient['quantity'] * person_count
                    ingredient_list[ingredient['ingredient_name']] = shop_list
                else:
                    ingredient_list[ingredient['ingredient_name']]['quantity'] = \
                        ingredient_list[ingredient['ingredient_name']]['quantity'] + \
                        ingredient['quantity'] * person_count
        else:
            print(f'\nТакого блюда нет - {dish_name}, '
                  f'введите другое значение из списка: \n {list(cook_book.keys())}')
    return ingredient_list

import os
def write_file(p1=None, p2=None, p3=None):
    if p1 or p2 or p3 is None:
        p1 = '1.txt'
        p2 = '2.txt'
        p3 = '3.txt'
        new_file = "rewrite_file.txt"
        path1 = os.path.join(os.getcwd(), p1)
        path2 = os.path.join(os.getcwd(), p2)
        path3 = os.path.join(os.getcwd(), p3)
        with open(path1, 'r', encoding='utf-8') as f1:
            text1 = f1.readlines()
        with open(path2, 'r', encoding='utf-8') as f2:
            text2 = f2.readlines()
        with open(path3, 'r', encoding='utf-8') as f3:
            text3 = f3.readlines()
        with open(new_file, 'w', encoding='utf-8') as f_new:
            if len(text1) < len(text2) \
                    and len(text1) < len(text3):
                f_new.write(p1 + '\n')
                f_new.write(str(len(text1)) + '\n')
                f_new.writelines(text1)
                f_new.write('\n')
            elif len(text3) < len(text1) \
                    and len(text3) < len(text2):
                f_new.write(p3 + '\n')
                f_new.write(str(len(text3)) + '\n')
                f_new.writelines(text3)
                f_new.write('\n')
            elif len(text2) < len(text1) and len(text2) < len(text3):
                f_new.write(p2 + '\n')
                f_new.write(str(len(text2)) + '\n')
                f_new.writelines(text2)
                f_new.write('\n')
            if len(text2) > len(text1) > len(text3) \
                    or len(text2) < len(text1) < len(
                    text3):
                f_new.write(p1 + '\n')
                f_new.write(str(len(text1)) + '\n')
                f_new.writelines(text1)
                f_new.write('\n')
            elif len(text1) > len(text3) > len(text2) \
                    or len(text3) > len(text1) and len(text3) < len(
                    text2):
                f_new.write(p3 + '\n')
                f_new.write(str(len(text3)) + '\n')
                f_new.writelines(text3)
                f_new.write('\n')
            elif len(text1) > len(text2) > len(text3) \
                    or len(text2) > len(text1) and len(text2) < len(
                    text3):
                f_new.write(p2 + '\n')
                f_new.write(str(len(text2)) + '\n')
                f_new.writelines(text2)
                f_new.write('\n')
            if len(text1) > len(text2) and len(text1) > len(text3):
                f_new.write(p1 + '\n')
                f_new.write(str(len(text1)) + '\n')
                f_new.writelines(text1)
            elif len(text2) > len(text1) and len(text2) > len(text3):
                f_new.write(p2 + '\n')
                f_new.write(str(len(text2)) + '\n')
                f_new.writelines(text2)
            elif len(text3) > len(text1) and len(text3) > len(text2):
                f_new.write(p3 + '\n')
                f_new.write(str(len(text3)) + '\n')
                f_new.writelines(text3)
    with open(new_file, 'r', encoding='utf-8') as file:
        file_read = file.read()
        print(file_read)
    return




print ('++++ Задание № 1 ++++')
cook_book = make_cook_book()
print(cook_book)
print()
print ('++++ Задание № 2 ++++')
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))
print()
print ('++++ Задание № 3 ++++')
write_file()
