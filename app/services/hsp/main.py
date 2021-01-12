import csv


def hsp_readers(csv_string_name):
    with open(csv_string_name, 'r') as file:

        reader = csv.DictReader(
            file
        )
        for hsp in reader:
            new_hsp = {}
            new_hsp.update({
                "city": hsp["NAME"],
                "uf": hsp["STATE"],
                "md_anual": hsp["ANNUAL"],
                "lon": hsp["LON"],
                "lat": hsp["LAT"]
            })

            yield new_hsp


for data in hsp_readers("hsp_data_2017.csv"):
    print(data)
