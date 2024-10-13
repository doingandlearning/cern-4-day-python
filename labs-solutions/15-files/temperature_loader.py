import csv

class TemperatureReading:
    """ Class representing temperature info """

    def __init__(self, temp, date, location, scale):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __str__(self):
        return f'TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})'

    def __repr__(self):
        return f'Temperature({self.temp}, {self.date}, {self.location}, {self.scale})'


def load_data(filename):
    data = []
    print('Loading file', filename)
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_length = len(row)
            if row_length != 4:
                print('Error in data (length is not 4):', row)
                print('In line:', reader.line_num)
            else:
                temp = float(row[0])
                scale = row[1]
                date = row[2]
                location = row[3]
                reading = TemperatureReading(temp, date, location, scale)
                data.append(reading)
    print('Finished reading file')
    return data


filename = input('Please enter the data file to load (data.csv): ')
if filename == '':
    filename = 'data.csv'

temperatures = load_data(filename)
print(temperatures)
