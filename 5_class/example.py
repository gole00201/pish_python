import argparse


def parse_line(row, line_no):
    def warn(msg):
        print("WARNING: " + msg)

    for elemt in row:
        elemt.strip()
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

with open(filename, "r", encoding="utf-8") as f:
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


# расчет статистики за год
def year_stats(line_datas):
    if not line_datas:
        print("WARNING: Нет данных для обработки")
        return None
    temp_middle = None
    temp_max = None
    temp_min = None  # Минимальная температура за год нам неизвестна
    temp_count = 0
    temp_sum = 0

    for line_data in line_datas:
        line_temp = line_data["temp"]
        temp_sum = temp_sum + line_temp

        temp_count = temp_count + 1

        # Если минимальная тмепература за год нам неизвестна или температура
        # в строке меньше чем минимальная температура за год, то
        # минимальная темпереатура за год равна темепаруре в этой строке

        if (temp_min is None) or (line_temp < temp_min):
            temp_min = line_temp
        if (temp_max is None) or (line_temp > temp_max):
            temp_max = line_temp

    temp_middle = temp_sum / temp_count

    return {
        "middle": temp_middle,
        "min": temp_min,
        "max": temp_max
    }


stats_for_year = year_stats(line_datas)

print()
print("**************СТАТИСТИКА ЗА ГОД****************")
print("МАКСИМАЛЬНАЯ: ", stats_for_year["max"])
print("МИНИМАЛЬНАЯ : ", stats_for_year["min"])
print("СРЕДНЯЯ     : ", stats_for_year["middle"])
print("***********************************************")
print()
# вывод на экран
