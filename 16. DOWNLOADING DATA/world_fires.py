from pathlib import Path
import pandas as pd
import plotly.express as px

class WorldFires:

    def __init__(self):
        self.file_path = 'world_fires/world_fires_1_day.csv'
        self.fire_data = None
        self.lats = []
        self.lons = []
        self.brightness = []
    
    def read_file(self):
        csv_path = Path(self.file_path)
        self.fire_data = pd.read_csv(csv_path)

    def extract_data(self):
        self.lats = self.fire_data['latitude'].tolist()
        self.lons = self.fire_data['longitude'].tolist()
        self.brightness = self.fire_data['brightness'].tolist()

    def plot_fire_data(self):
        fig = px.scatter_geo(lat=self.lats, lon=self.lons, size=self.brightness, title="Global Fire Incidents",
                     color=self.brightness,
                     color_continuous_scale='YlOrRd',
                     labels={'color':'Brightness'},
                     projection='aitoff',
                     hover_name=self.brightness,
                     )
        fig.show()
    
    def run(self):
        self.read_file()
        self.extract_data()
        self.plot_fire_data()

if __name__ == '__main__':
    Data = WorldFires()
    Data.run() 