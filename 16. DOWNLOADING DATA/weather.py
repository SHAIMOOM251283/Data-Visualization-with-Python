from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

class Weather:

    def __init__(self):
        self.file_path = 'weather_data/sitka_weather_07-2021_simple.csv'
        self.reader = None
        self.header_row = None
        self.date_index = None
        self.tmin_index = None
        self.tmax_index = None
        self.station_name = None
        self.dates = []
        self.highs = []
        self.lows = []

    def create_reader_object(self):
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
        self.tmin_index = self.header_row.index('TMIN')
        self.tmax_index = self.header_row.index('TMAX')
    
    def extract_station_name_from_header_row(self):
        second_row = next(self.reader)
        self.station_name = second_row[1]
        print(f"Station name: {self.station_name}")
    
    def extract_weather_data(self):
        for row in self.reader:
            current_date = datetime.strptime(row[self.date_index], '%Y-%m-%d')
            try:
                high = int(row[self.tmax_index])
                low = int(row[self.tmin_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                self.dates.append(current_date)
                self.highs.append(high)
                self.lows.append(low)
    
    def plot_weather_data(self):
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(self.dates, self.highs, color='red', alpha=0.5)
        ax.plot(self.dates, self.lows, color='blue', alpha=0.5)
        ax.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.1)

        ax.set_title(f"Daily High and Low Temperatures, 2021\n{self.station_name}", fontsize=20)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()

        ax.set_ylabel("Temperature (F)", fontsize=16, fontweight='bold', color='darkblue')
        ax.tick_params(axis='y', labelsize=14, colors='darkblue')
        ax.set_ylim(10, 140)  # Setting y-axis limits to accommodate both Sitka and Death Valley
        ax.set_yticks(range(10, 141, 10))
        ax.set_yticklabels([f"{t}°F" for t in range(10, 141, 10)], fontsize=12, color='darkblue') 

        plt.show()
    
    def run(self):
        self.create_reader_object()
        self.print_indexes()
        self.extract_indexes()
        self.extract_station_name_from_header_row()
        self.extract_weather_data()
        self.plot_weather_data()

if __name__ == '__main__':
    Data = Weather()
    Data.run()