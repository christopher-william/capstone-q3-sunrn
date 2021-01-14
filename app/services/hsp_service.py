import csv
import psycopg2


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


def populating_hsp():
    conn = psycopg2.connect(
        "dbname=dendondkajlok4 user=ifpozknijmezbg password=2950811ec54934a8793f053c3b1d8851c517f66b6a7f67c64c7f1d168c80050b host=ec2-107-22-14-60.compute-1.amazonaws.com port=5432")

    cur = conn.cursor()

    for data in hsp_readers("hsp_data_2017.csv"):

        cur.execute("INSERT INTO hsp (city,uf,md_anual,lon,lat) VALUES(%s,%s,%s,%s,%s)",
                    (data["city"], data["uf"], data["md_anual"], data["lon"], data["lat"]))

        conn.commit()
    cur.close()
    conn.close()


populating_hsp()
