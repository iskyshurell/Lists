def func(i_elem):
    additional = [i_num for i_num in range( 1 + i_elem, 10 + i_elem, 4 )]
    return additional

list = [
        func(i_elem)

        for i_elem in range(4)
         ]

print(list)