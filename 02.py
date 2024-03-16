import random
import csv


def quicksort(nums: str):
    """
    Быстрая сортировка, сортирует за 0(nlogn)

    Описание параметров:
    nums: названия компаний
    """

    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n > q:
                s_nums.append(n)
            elif n < q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


with open("devices.csv", encoding="utf-8") as inp:
    csv_reader = csv.DictReader(inp, delimiter="*")
    companies = set()
    company_product_price = {}
    for row in csv_reader:
        company = row["Company"]
        company_product_price[company] = row
        companies.add(company)
    companies = list(companies)
    sorted_companies = quicksort(companies)
    for company in sorted_companies[:5]:
        product = company_product_price[company]["Product"]
        price = company_product_price[company]["Price"]
        print(f"{company} - {product} - {price}")


# так и не понял условие, поэтому вывел рандомную информацию по пяти отсортированным компаниям 
