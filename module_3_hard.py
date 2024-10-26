data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    res = 0
    if isinstance(data_structure, int):
        res += data_structure
    elif isinstance(data_structure, str):
        res += len(data_structure)
    elif isinstance(data_structure, list) or isinstance(data_structure, tuple) or isinstance(data_structure, set):
        for item in data_structure:
            res += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            res += calculate_structure_sum(key)
            res += calculate_structure_sum(value)

    return res


result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99
