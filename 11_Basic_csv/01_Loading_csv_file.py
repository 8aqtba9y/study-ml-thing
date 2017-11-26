import csv, codecs

# use pandas instead of csv with codecs
filename = "00_csv_file.csv"
file = codecs.open(filename, "r", "shift-jis")

reader = csv.reader(file, delimiter=",") # 3rd parameter: quotechar='"'
for cells in reader:
    print(cells[1], cells[2])
