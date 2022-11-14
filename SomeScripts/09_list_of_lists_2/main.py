nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

sorted_list = [i_elem
               for i_list1 in nice_list
               for i_list2 in i_list1
               for i_elem in i_list2]
print(sorted_list)
