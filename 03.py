import csv


def bin_search(name_to_find: str, sorted_data: list) -> dict:
    """
    Бинарый поиск для быстрого нахождения подходящх параметров

    Описание аргументов:
    name_to_find - значение, которое надо найти в отсортированном списке
    sorted_data - отсортированный массив компаний (по названию)

    Возвращает словарь с параметрами товара
    """

    left, right = 0, len(sorted_data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_data[mid][0].lower() == name_to_find.lower():
            return sorted_data[mid][1]
        elif sorted_data[mid][0].lower() < name_to_find.lower():
            left = mid + 1
        else:
            right = mid - 1
    return {}


with open("devices.csv", encoding="utf-8") as inp:
    csv_reader = csv.DictReader(inp, delimiter="*")
    company_most_expensive = {}
    for row in csv_reader:
        company = row["Company"]
        if company not in company_most_expensive:
            company_most_expensive[company] = row
        else:
            price_last = float(company_most_expensive[company]["Price"].replace(",", "."))
            price_now = float(row["Price"].replace(",", "."))
            if price_now > price_last:
                company_most_expensive[company] = row

    company_most_expensive = list(company_most_expensive.items())
    company_most_expensive.sort(key=lambda x: x[0].lower())
    inserted_company = input("Введите желаемую компанию: ")
    while inserted_company != "=":
        out = bin_search(inserted_company, company_most_expensive)
        if out:
            print(f"По вашему запросу: {inserted_company} найдены следующие варианты:")
            print(f"{out["Company"]} {out["Product"]} - тип устройства: {out["TypeName"]};")
            print(f"Разрешение экрана - {out["Inches"]};\nЦена - {out["Price"]}")
        else:
            print(f"По вашему запросу: {inserted_company} ничего не найдено(")
        inserted_company = input("Введите желаемую компанию: ")
