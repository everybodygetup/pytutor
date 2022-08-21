list = [2, 3, 5, 3, 7, 9, 5, 3, 7]  # обозначаем


def second_sort(list):
    list.sort()  # сортируем
    return sorted(list, key=list.count, reverse=True)


result = second_sort(list)
print(result)
