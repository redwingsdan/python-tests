import csv

def writer (header, data, filename, option):
    with open (filename, 'w', newline = '') as csvfile:
        if option == 'write':
            pizza_places = csv.writer(csvfile)
            pizza_places.writerow(header)
            for data_row in data:
                pizza_places.writerow(data_row)
        elif option == 'update':
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print('Unknown option')

def updater(filename):
    with open(filename, 'r', newline = '') as csvfile:
        readData = [row for row in csv.DictReader(csvfile)]
        readData[0]['Rating'] = '9.2'
    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, 'update')

csvFileName = 'csv_pizza_ratings.csv'
csvHeader = ('Rank', 'Rating', 'Pizza Place')
csvData = [
    (1, 9.4, 'Di Faras'),
    (2, 8.8, 'Frank Pepes'),
    (3, 7.3, 'Pizza District'),
    (4, 6.9, 'Poppa Ginos')
]
writer(csvHeader, csvData, csvFileName, 'write')
updater(csvFileName)