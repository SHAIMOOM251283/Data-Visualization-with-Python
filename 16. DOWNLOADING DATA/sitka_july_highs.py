from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

class Weather:

    def __init__(self):
        self.file_path = 'weather_data/sitka_weather_07-2021_simple.csv'
        self.reader = None
        self.header_row = None
        self.station_name = None
        self.dates = []
        self.highs = []
    
    def create_reader_object(self):
        path = Path(self.file_path)
        lines = path.read_text().splitlines()
        self.reader = csv.reader(lines)
        self.header_row = next(self.reader)
        print(self.header_row)
    
    def print_indexes(self):
        for index, column_header in enumerate(self.header_row):
            print(index, column_header)
    
    def exract_station_name(self):
        second_row = next(self.reader)
        self.station_name = second_row[1]
        print(f"Station name: {self.station_name}")
    
    def extract_weather_data(self):
        for row in self.reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[4])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                self.dates.append(current_date)
                self.highs.append(high)
    
    def plot_weather_data(self):
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(self.dates, self.highs, color='red')

        ax.set_title(f"Daily High Temperatures, July 2021\n{self.station_name}", fontsize=20)
        ax.set_xlabel('', fontsize=16)
        #ax.tick_params(axis='x', labelsize=12, colors='darkblue')
        fig.autofmt_xdate()

        ax.set_ylabel("Temperature (F)", fontsize=16, fontweight='bold', color='darkblue')
        ax.tick_params(axis='y', labelsize=16, colors='darkblue')
        
        plt.show()
    
    def run(self):
        self.create_reader_object()
        self.print_indexes()
        self.exract_station_name()
        self.extract_weather_data()
        self.plot_weather_data()

if __name__ == '__main__':
    Data = Weather()
    Data.run()