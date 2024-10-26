def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, 'текст', False)

values_list = [2, 'Артём', False]
values_dict = {'a': 888, 'b': 'Хай', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54, 'Строка']
print_params(*values_list_2, 42)