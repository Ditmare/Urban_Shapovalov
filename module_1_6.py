#Словари
my_dict = {'Artem': 2005, 'Nina': 2005, 'Viktoriya': 2004}
print('Dict:', my_dict)
print('Existing value:', my_dict['Nina'])
print('Not existing value:', my_dict.get('Valera'))
my_dict.update({'Sanya': 1997, 'Masha': 2000})
a = my_dict.pop('Masha')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
#Множества
my_set = {1, 2, 3, 1, 2, 3, 'Nina', 'Artem', 'Nina'}
print('Set:', my_set)
my_set.update(['Car'], ['House'])
my_set.remove(2)
print('Modified set:', my_set)