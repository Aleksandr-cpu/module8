def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    count = 0
    if not isinstance(numbers, (list, tuple)):
        print("В numbers записан некорректный тип данных")
        return None
    for number in numbers:
        if not isinstance(number, (int, float)):
            print(f"В {number} записан некорректный тип данных")

        else:
            count +=1
    total_sum, incorrect_data = personal_sum(numbers)

    if incorrect_data < 0:
        print(f"В {numbers} записан некорректный тип данных")
        return 0

    try:
        average = total_sum / count
    except ZeroDivisionError:
        average = 0

    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')