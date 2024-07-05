from pathlib import Path
import json
import pandas as pd
import plotly.express as px

class Earthquakes:

    def __init__(self):
        self.file_path = 'eq_data/eq_data_30_day_m1.geojson'
        self.all_eq_data = None
        self.title = None
        self.all_eq_dicts = None
        self.df = None
        self.mags = []
        self.lons = []
        self.lats = []
        self.eq_titles = []

    def create_object(self):
        path = Path(self.file_path)
        contents = path.read_text(encoding="utf-8")
        self.all_eq_data = json.loads(contents)

    def extract_title_from_metadata(self):
        self.title = self.all_eq_data['metadata']['title']
        print(self.title)

    def examine_all_earthquakes_in_the_dataset(self):
        self.all_eq_dicts = self.all_eq_data['features']
        print(f"\nEARTHQUAKES IN THE DATASET: {len(self.all_eq_dicts)}")

    def extract_data(self):
        data = {
            'magnitude': [eq['properties']['mag'] for eq in self.all_eq_dicts],
            'longitude': [eq['geometry']['coordinates'][0] for eq in self.all_eq_dicts],
            'latitude': [eq['geometry']['coordinates'][1] for eq in self.all_eq_dicts],
            'title': [eq['properties']['title'] for eq in self.all_eq_dicts]
            }

        self.df = pd.DataFrame(data)

    def extract_lists_using_tolist_method(self):
        self.mags = self.df['magnitude'].tolist()
        self.lons = self.df['longitude'].tolist()
        self.lats = self.df['latitude'].tolist()
        self.eq_titles = self.df['title'].tolist()

        print(f"\nEARTHQUAKES IN THE DATASET: {len(self.df)}")
        print(f"\nMAGNITUDES: {self.mags[:10]}")
        print(f"\nLONGITUDES: {self.lons[:5]}")
        print(f"\nLATITUDES: {self.lats[:5]}")

    def create_the_scatter_plot(self):
        fig = px.scatter_geo(lat=self.lats, lon=self.lons, size=self.mags, title=self.title,
                     color=self.mags,
                     color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='hammer',
                     hover_name=self.eq_titles,
                     )
        fig.show()
    
    def run(self):
        self.create_object()
        self.extract_title_from_metadata()
        self.examine_all_earthquakes_in_the_dataset()
        self.extract_data()
        self.extract_lists_using_tolist_method()
        self.create_the_scatter_plot()

if __name__ == '__main__':
    Data = Earthquakes()
    Data.run()
