# азы

for line in range(1, 11):
    row_line = ""
    for num in range(1, 11):
        row_line = f"{row_line}\t{num * line}"

    print(row_line)

for line in range(1, 21):
    row_line = ""
    for column in range(1, 21):
        row_line = f"{row_line}\t{line*column}"

    print(row_line)

# продолжение

if True and count == 1 and count == 2:
    print("if")
elif count == "count":
    print("first elif")
elif count == 14.2:
    print("second elif")
elif count == 1:
    print("nth elif")
else:
    print("else")


# Пропишем и присвоим ряд
list1 = [1, 5, 78, 36, -45, -3, 46]
print("list =", list1)
# Выберем наименьшее
num = min(list1)
print("наименьшее число =", num)

# Сортировка
list1 = [1, 5, 78, 36, -45, -3, 46]
print("list =", list1)
list1.sort()
print("smallest number =", list1)
