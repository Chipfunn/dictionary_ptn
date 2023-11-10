# Словари

# Создаем англо-русский словарь
# Ключ- слово на английском языке
# Значение - слово на русском языке

english_dict={
    'apple':'яблоко',
    'milk':'молоко',
    'cat':'кот'
}
print(english_dict)
russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely']
)
print(russian_dict)
# Определение количества элементов в словаре
#       len(название_словаря)
print(len(russian_dict))
# Обращение к элементу словаря по ключу
#       название_словаря[ключ]
#       название_словаря[ключ]

print(english_dict["apple"])

word=input("Введите слово")

if word in russian_dict:
    print(russian_dict[word])
    for i in range(len(russian_dict[word])):
        print(russian_dict[word][i])
else:
    print("такого слова нет")

print(russian_dict["кошка"])







# Обращение к элементу словаря с помощью метода get()
# get() - возвращает значение по ключу, если такой ключ есть в словаре
# в противном случае возвращает None

word=input("ведите слово")
print(english_dict.get(word))

#вывод элементов словаря с помощью цикла
#for key in название_словаря:print(key)

for key in english_dict:
    print(key)
    print(english_dict[key])