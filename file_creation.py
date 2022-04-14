import csv

def create_file(city, humidity, pressure, wind):
    with open("csv_folder.csv", "a", errors="ignore", newline="") as csv_file:
        writter = csv.writer(csv_file)
        writter.writerow([city, humidity, pressure, wind])



