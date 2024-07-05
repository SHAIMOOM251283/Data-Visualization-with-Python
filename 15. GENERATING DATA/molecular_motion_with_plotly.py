import plotly.graph_objs as go
from random import choice

class RandomWalk:

    def __init__(self):
        self.num_points = None
        self.x_step = None
        self.y_step = None
        self.x_values = []
        self.y_values = []

    def points(self):
        self.num_points = int(input("Enter Points: "))
    
    def get_x_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        self.x_step = x_direction * x_distance
    
    def get_y_step(self):
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        self.y_step = y_direction * y_distance
    
    def fill_walk(self):
        self.x_values = [0] 
        self.y_values = [0] 

        while len(self.x_values) < self.num_points:

            self.get_x_step()
            self.get_y_step()

            if self.x_step == 0 and self.y_step == 0:
                continue

            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step

            self.x_values.append(x)
            self.y_values.append(y)
        
    def walk(self):
        point_numbers = list(range(len(self.x_values)))

        scatter = go.Scatter(
            x=self.x_values,
            y=self.y_values,
            mode='markers',
            marker=dict(
                size=5,
                color=point_numbers,
                colorscale='Blues',
                showscale=True
            )
        )

        start_point = go.Scatter(
            x=[self.x_values[0]],
            y=[self.y_values[0]],
            mode='markers',
            marker=dict(
                size=12,
                color='green'
            ),
            name='Start'
        )

        end_point = go.Scatter(
            x=[self.x_values[-1]],
            y=[self.y_values[-1]],
            mode='markers',
            marker=dict(
                size=12,
                color='red'
            ),
            name='End'
        )

        layout = go.Layout(
            title='Random Walk',
            showlegend=True,
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            width=1000,
            height=700
        )

        fig = go.Figure(data=[scatter, start_point, end_point], layout=layout)
        fig.show()

    def run(self):
        while True:
            self.points()
            self.get_x_step()
            self.get_y_step()
            self.fill_walk()
            self.walk()

            keep_running = input("Make another walk? (y/n): ")
            if keep_running == 'n':
                break

if __name__ == "__main__":
    rw = RandomWalk()
    rw.run()
