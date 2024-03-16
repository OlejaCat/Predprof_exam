import csv


with open("devices.csv", encoding="utf-8") as inp:
    csv_reader = csv.DictReader(inp, delimiter="*")
    company_with_product_price = {}
    for row in csv_reader:
        company = row["Company"]
        product = row["Product"]
        price = row["Price"]
        company_with_product_price[f"{company} {product}"] = price
    for idx, item in enumerate(company_with_product_price.items(), start=1):
        key, value = item
        print(key, value)
        if idx == 10:
            break