import csv


with open("devices.csv", encoding="utf-8") as inp:
    csv_reader = csv.DictReader(inp, delimiter="*")
    company_salary = {}
    notebooks = ["Ultrabook", "Notebook", "Netbook"]
    for row in csv_reader:
        company = row["Company"]
        price = float(row["Price"].replace(",", "."))
        type_name = row["TypeName"]
        if type_name in notebooks:
            if company not in company_salary:
                company_salary[company] = 0.0
            company_salary[company] += price

    for company, salary in company_salary.items():
        print(f"Если продать все ноутбуки {company} можно заработать {salary}")
