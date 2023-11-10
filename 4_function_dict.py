# Дополнительные полезные функции и методы словарей
# Метод keys() - возвращает список ключей словаря
# Метод values() - возвращает список значений словаря
# Метод items() - возвращает список из пар (кортежи) ключ- значение

russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely']
)
print(russian_dict.keys())
print("-"*100)
print(russian_dict.values())
print("-"*100)
print(russian_dict.items())
print("-"*100)


#Вывод всех ключей словаря
#for key in название_словаря: print(key)

for key in russian_dict:
    print(key)

#Вывод всех значений
#for value in название_словаря.values(): print(value)

for value in russian_dict.values():
    print(value)


#Вывод всех пар «ключ / значение»
#for key,value in название_словаря.items(): print(key,value)

for key,value in russian_dict.items():
    print(key,value)





# Метод copy()  - возвращает копию указанного  словаря

new_dict = russian_dict.copy()
print(new_dict["кошка"])


# Метод clear() - полностью очищает словарь (удаляет все пары ключ-значение)

russian_dict.clear()

# создание нового словаря  из  последовательности key и значениями value. По умолчанию value присваивается значение None.
#название_словаря=dict.fromkeys(['ключ1', 'ключ2','ключ3'],value)

russian_dict=dict.fromkeys(['ключ1', 'ключ2','ключ3'],0)
print(russian_dict)


