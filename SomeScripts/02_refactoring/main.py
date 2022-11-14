

def gen_find(list_1, list_2, to_find):
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to_find:
                yield (x, y)

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


print(next(gen_find(list_1, list_2, to_find)))


