import csv


with open("devices.csv", encoding="utf-8") as inp:
    csv_reader = csv.DictReader(inp, delimiter="*")
    notebook_types = {}
    for row in csv_reader:
        notebook = row["TypeName"]
        if notebook not in notebook_types:
            notebook_types[notebook] = {}
        ram_size = row["Ram"]
        if ram_size not in notebook_types[notebook]:
            notebook_types[notebook][ram_size] = 0
        notebook_types[notebook][ram_size] += 1

    with open("count_company.txt", "w") as out_file:
        notebooks_to_search = ["Ultrabook", "Notebook", "Netbook"]
        for notebook in notebooks_to_search:
            out_file.write(f"{notebook}\n")
            for ram_size, counter in notebook_types[notebook].items():
                out_file.write(f"{ram_size} - {counter}\n")

