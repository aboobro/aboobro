# data typelariga qarab ajratuvchi dastur
new_list = [14, 56, "salom", "hammaga", {12, "salom"}, (8, 87)]
int_list = ["int"]
str_list = ["str"]
set_list = ["set"]
tuple_list = ["tuple"]
for element in new_list:
    if type(element) == int:
        int_list.append(element)
    elif type(element) == str:
        str_list.append(element)
    elif type(element) == tuple:
        tuple_list.append(element)
    elif type(element) == set:
        set_list.append(element)
    else:
        print("")

print(int_list)
print(str_list)
print(set_list)
print(tuple_list)