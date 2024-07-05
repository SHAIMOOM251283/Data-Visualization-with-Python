from pathlib import Path
import json
import plotly.express as px

class Earthquakes:

    def __init__(self):
        self.file_path = 'eq_data/recent_eq.geojson'
        self.all_eq_data = None
        self.title = None
        self.all_eq_dicts = None
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
        for eq_dict in self.all_eq_dicts:
            self.mags.append(eq_dict['properties']['mag'])
            self.lons.append(eq_dict['geometry']['coordinates'][0])
            self.lats.append(eq_dict['geometry']['coordinates'][1])
            self.eq_titles.append(eq_dict['properties']['title'])

        print(f"\nMAGNITUDES: {self.mags[:10]}")
        print(f"\nLONGITUDES: {self.lons[:5]}")
        print(f"\nLATITUDES: {self.lats[:5]}")

    def create_scatter_plot(self):
        fig = px.scatter_geo(lat=self.lats, lon=self.lons, size=self.mags, title=self.title,
                     color=self.mags,
                     color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='orthographic',
                     hover_name=self.eq_titles,
                     )
        fig.show()

    def run(self):
        self.create_object()
        self.extract_title_from_metadata()
        self.examine_all_earthquakes_in_the_dataset()
        self.extract_data()
        self.create_scatter_plot()

if __name__ == '__main__':
    Data = Earthquakes()
    Data.run()
