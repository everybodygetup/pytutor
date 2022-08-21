def print_check(all_positions):
    sum = 0  # переменная для накопления общей суммы
    print("AutoTravel")
    # в цикле будем выводить название, количество и цену
    for travel in all_positions:
        name = travel[0]
        amount = travel[1]
        price = travel[2]
        print(f"{name} ({amount} шт.) - {price} руб.")
        sum += amount * price  # здесь будем считать общую сумму
    print(f"\nИтого: {sum} руб.")
    print("Спасибо что выбрали нас!")


# (название, количество суток или посещений, цена за сутки или сеанс)
all_positions = [
    ("hotel RoadHell", 3, 2000),
    ("hotel RadissonRussia", 1, 10000),
    ("Мавзолей Ленин", 1, 500),
    ("Кафе Удача", 1, 3000),
]
# print_check(all_positions)
