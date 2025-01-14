import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    module = getattr(obj, '__module__', None)

    additional_info = {}

    if isinstance(obj, (int, float)):
        additional_info['is_integer'] = isinstance(obj, int)
        additional_info['is_float'] = isinstance(obj, float)
    elif isinstance(obj, str):
        additional_info['length'] = len(obj)
    elif isinstance(obj, list):
        additional_info['length'] = len(obj)
        additional_info['is_empty'] = len(obj) == 0
    elif isinstance(obj, dict):
        additional_info['length'] = len(obj)
        additional_info['is_empty'] = len(obj) == 0

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'additional_info': additional_info
    }


class MyClass:
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 = "value2"

    def method1(self):
        pass

    def method2(self):
        pass


my_object = MyClass()
object_info = introspection_info(my_object)
print(object_info)

number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)

dict_info = introspection_info({'key': 'value'})
print(dict_info)