import os
from operator import itemgetter


def main(t_len = 0,
         alphabet =
            ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"],
                sym_dict = {}):

    for string in open("text.txt", "r"):
        for i_sym in string:
            temp = action(t_len, i_sym, alphabet, sym_dict)
            sym_dict = temp[0]
            t_len = temp[1]

    return (sym_dict, t_len)

def action(t_len, i_sym, alphabet, sym_dict):
    if i_sym.lower() in alphabet:
        t_len += 1
        if i_sym.lower() in sym_dict:
            sym_dict[i_sym.lower()] += 1
        else:
            sym_dict[i_sym.lower()] = 1

        return (sym_dict, t_len)

def sorting_main(sym_dict, sym_list = []):
    for i_key, i_value in sym_dict.items():
        sym_list.append((i_key, i_value))

    new_dict = sorting_alphabet(sym_list)
    new_dict = sorting_numbers(new_dict)
    return new_dict
        
def sorting_alphabet(sym_list):
    return sorted(sym_list, key = itemgetter(0))

def sorting_numbers(new_dict):
    for index in range(len(new_dict) - 1):
        if new_dict[index][1] < new_dict[index + 1][1]:
            elem = new_dict.pop(index + 1)
            new_dict.insert(index, elem)

    return new_dict

def saving_results(t_len, new_dict):
    file = open("analysis.txt", "w")

    for i_elem in new_dict:
        file.write(f"{i_elem[0]} - {round(i_elem[1] / t_len, 3)}\n")

    file.close()


temp = main()
sym_dict = temp[0]
text_len = temp[1]

new_dict = sorting_main(sym_dict)
saving_results(text_len, new_dict)