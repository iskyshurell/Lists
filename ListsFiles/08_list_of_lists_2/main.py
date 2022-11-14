nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
end_list = []

def really_nice_list(new_list = nice_list, end = end_list):
    for i_elem in new_list:
        if isinstance(i_elem, list):
            really_nice_list(new_list = i_elem)
        else:
            end.append(i_elem)

really_nice_list()
print(end_list)