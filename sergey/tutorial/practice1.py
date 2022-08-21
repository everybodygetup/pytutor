# Первое задание первая практика: развернуть слово

string1 = "world"[::-1]
print(string1)
# срез 1


def reverse_string1(l):
    return l[::-1]
    print(reverse_string1(" world"))


# срез 2

# Второе задание первая практика: сортировать ряд чисел

list = [2, 3, 5, 3, 7, 9, 5, 3, 7]  # обозначаем


def second_sort(list):
    list.sort()  # сортируем
    return sorted(list, key=list.count, reverse=True)


result = second_sort(list)
print(result)

# Третье задание первая практика: Жаргон падонкаф


def get_string_pad(string):
    for i, l in enumerate(string):  # пронумировали
        if i % 2:  # четные нечетныеgit
            print(l.upper(), end="")
        else:
            print(l.lower(), end="")
