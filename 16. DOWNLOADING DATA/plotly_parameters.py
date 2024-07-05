import plotly.express as px

class Sample:

    def __init__(self):
        self.lats = [34.0522, 40.7128, 37.7749]
        self.lons = [-118.2437, -74.0060, -122.4194]
        self.mags = [4.5, 5.0, 4.8]
        self.eq_titles = ["Los Angeles", "New York", "San Francisco"]

    def plot(self):
        fig = px.scatter_geo(lat=self.lats, lon=self.lons, size=self.mags, title="Earthquakes",
                     color=self.mags, color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='azimuthal equidistant',
                     hover_name=self.eq_titles,
                     size_max=15  # Example of size scaling parameter
                    )

        fig.show()

if __name__ == '__main__':
    Data = Sample()
    Data.plot()