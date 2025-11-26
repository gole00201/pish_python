import argparse


def parse_line(row, line_no):
    def warn(msg):
        print("WARNING: " + msg)

    for i in range(len(row)):
        row[i] = row[i].strip()

    try:
        year = int(row[0])
        month = int(row[1])
        day = int(row[2])
        hour = int(row[3])
        minute = int(row[4])
        temperature = int(row[5])
    except Exception:
        warn("Строка {}: не удалось преобразовать поля в числа -> пропуск.  Строка: {}".format(
            line_no, row))
        return None

    return {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "temp": temperature,
    }


parser = argparse.ArgumentParser(
    description="Приложение для вычисления статистики температуры из CSV-файла."
)

parser.add_argument(
    "-f",
    "--file",
    help="Входной CSV-файл",
    required=False
)

parser.add_argument(
    "-m",
    "--month",
    type=int,
    help="Номер месяца (1..12) для вывода статистики только по нему",
    required=False
)

args = parser.parse_args()

if args.file is None:
    parser.print_help()
    exit()

filename = args.file
month_filter = args.month

if month_filter is not None:
    if not (1 <= month_filter <= 12):
        print("Ошибка: номер месяца должен быть от 1 до 12.")
        exit()

line_datas = []

with open(filename) as f:
    line_number = 0
    for line in f:
        line_number += 1
        line = line.strip()

        if line == "":
            continue

        row = line.split(";")
        line_data = parse_line(row, line_number)
        if line_data is not None:
            line_datas.append(line_data)

def year_stats(datas):
    if not datas:
        print("WARNING: Нет данных для обработки")
        return None

    temp_count = 0
    temp_sum = 0

    temp_max = None
    temp_min = None  # Минимальная температура неизвестна
    temp_avg = None

    for line in datas:
        new_temp = line['temp']
        temp_sum = temp_sum + new_temp
        temp_count = temp_count + 1

        # Если минимальная температура неизвестна или же текущая
        # температура меньше чем ИЗВЕСТНАЯ минимальная,
        # то я нашел новую минимальную температуру

        if (temp_min is None) or (new_temp < temp_min):
            temp_min = new_temp

        if (temp_max is None) or (new_temp > temp_max):
            temp_max = new_temp

    temp_avg = temp_sum / temp_count

    return {
        "avg": temp_avg,
        "max": temp_max,
        "min": temp_min
    }

# Посчитать месяца

# 1. Сделать две функции. Одна функция на случай если пользователь хочет 1 месяц
# Вторая функция на случай если нужно обработать все

# 2. Одна функция на все

def mounth_stats(datas):
    pass

year_data = year_stats(line_datas)
print()
print("================ГОД=================")
print("СРЕДНЯЯ:      ", year_data['avg'])
print("МАКСИМАЛЬНАЯ: ", year_data['max'])
print("МИНИМАЛЬНАЯ:  ", year_data['min'])
print("====================================")
print()