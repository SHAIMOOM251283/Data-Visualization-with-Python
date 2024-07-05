from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

class Weather:

    def __init__(self):
        self.file_path = 'weather_data/sitka_weather_2021_full.csv'
        self.reader = None
        self.header_row = None
        self.station_name = None
        self.date_index = None
        self.rainfall_index = None
        self.dates = []
        self.rainfall = []

    def initialize_reader_object(self):
        path = Path(self.file_path)
        lines = path.read_text().splitlines()
        self.reader = csv.reader(lines)
        self.header_row = next(self.reader)
        print(self.header_row)
    
    def print_indexes(self):
        for index, column_header in enumerate(self.header_row):
            print(index, column_header)
        
    def extract_indexes(self):
        self.date_index = self.header_row.index('DATE')
        self.rainfall_index = self.header_row.index('PRCP')
    
    def extract_station_name(self):
        second_row = next(self.reader)
        self.station_name = second_row[1]
        print(f"Station name: {self.station_name}")

    def extract_weather_data(self):
        for row in self.reader:
            current_date = datetime.strptime(row[self.date_index], '%Y-%m-%d')
            PRCP = float(row[self.rainfall_index])
            self.dates.append(current_date)
            self.rainfall.append(PRCP)
    
    def plot_weather_data(self):
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(self.dates, self.rainfall, color='red')

        ax.set_title(f"Daily Rainfall, 2021\n{self.station_name}", fontsize=20)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        
        ax.set_ylabel("PRCP", fontsize=16)
        ax.tick_params(labelsize=16)
        
        plt.show()

    def run(self):
        self.initialize_reader_object()
        self.print_indexes()
        self.extract_indexes()
        self.extract_station_name()
        self.extract_weather_data()
        self.plot_weather_data()

if __name__ == '__main__':
    Data = Weather()
    Data.run()
