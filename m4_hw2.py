try:
    with open('cats_info.txt', 'w') as cats:
        cats.write('60b90c1c13067a15887e1ae1,Tayson,3\n\
                    60b90c2413067a15887e1ae2,Vika,1\n\
                    60b90c2e13067a15887e1ae3,Barsik,2\n\
                    60b90c3b13067a15887e1ae4,Simon,12\n\
                    60b90c4613067a15887e1ae5,Tessi,5\n')
except IOError as e:
    print(f"Error read file: {e}")


def get_cats_info(path):
    with open(path) as cats_list:
        lines_list = [el.strip() for el in cats_list.readlines() if el.strip()]
    new_list = []
    for cat in lines_list:
        try:
            cat_lst = cat.split(',')
            if len(cat_lst) != 3:
                raise ValueError("Invalid string format in file")
            dict_cats = {"id": cat_lst[0], "name": cat_lst[1], "age": int(cat_lst[2])}
            new_list.append(dict_cats)
        except ValueError as e:
            print(f"an error occurred while processing the file: {e}")
            return []
    return new_list


try:
    cats_info = get_cats_info('cats_info.txt')
    print(cats_info)
except FileNotFoundError as e:
    print(f"Error: {e}")