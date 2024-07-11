

def introspection_info(obj):
    # - Тип объекта
    print('type: ', type(obj))
    # - Атрибуты объекта.
    _attributes = [a for a in dir(obj) if a.startswith("__")]
    print('attributes: ', dir(obj))
    # - Методы объекта.
    _methods = [b for b in dir(obj) if not b.startswith("__")]
    print('methods: ',_methods)
    # - Модуль, к которому объект принадлежит.
    print('module: ', __name__ )
    # - адрес объекта в памяти
    print('id:', id(obj))



number_info = introspection_info(42)
print(number_info)

