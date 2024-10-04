mutable_var = (1, 2, 3, 'word', 2.3)
print(mutable_var)
#mutable_var[3] = 'delete' ошибка, так как кортеж неизменяем, не поддерживает обращение по элементам(кроме списка внутри)
mutable_list = [1, 2, 3, 'word', 2.3]
print(mutable_list)
mutable_list[3] = 'dsf'
print(mutable_list)

