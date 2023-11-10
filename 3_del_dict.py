# Удаление из словаря
# 1)Оператор del - удаляет элемент по указанному ключу
#       del название_словаря[ключ]
# 2)Метод pop - удаляет и возвращает элемент по указанному ключу
#       название_словаря.pop(ключ)
# 3)Метод popitem() - удаляет и возвращает последний по порядку элемент
#       название_словаря.popitem()

russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely'],
    собака=["dog"],
)
item=input("введите искомое слово")
if item in russian_dict:
    del russian_dict[item]

del russian_dict["кошка"]
russian_dict.pop("красивый")
result = russian_dict.popitem()
print(result)
